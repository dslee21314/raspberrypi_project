import RPi.GPIO as GPIO
import datetime
import time
import cv2
from inference import Roboflow
from notify import LineNotify

# 設定 GPIO 模式
GPIO.setmode(GPIO.BCM)

# 設定 GPIO 23 (Trig) 和 GPIO 24 (Echo)
TRIG = 23
ECHO = 24

IMG_HEIGHT = 480
IMG_WIDTH = 640

# 設定 GPIO 23 為輸出模式，GPIO 24 為輸入模式
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

# 初始化 OpenCV 相機
cap = cv2.VideoCapture(0)  # 使用 Pi Camera 或 USB 相機

roboflow = Roboflow()


if not cap.isOpened():
    print("無法啟動相機")
    exit()

# 設定攝像頭的預覽尺寸
cap.set(3, 640)  # 設定畫面寬度
cap.set(4, 480)  # 設定畫面高度
pred_result = {}

def get_distance():
    # 發送 10us 的脈衝到 Trig 腳位
    GPIO.output(TRIG, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TRIG, GPIO.LOW)
    
    # 等待 Echo 腳位變高並計算持續時間
    while GPIO.input(ECHO) == GPIO.LOW:
        pulse_start = time.time()
    
    while GPIO.input(ECHO) == GPIO.HIGH:
        pulse_end = time.time()
    
    # 計算時間差並轉換為距離 (聲音速度約為 343米每秒)
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150  # 17150 是從秒轉換為厘米的常數
    return distance

def stream_preview(pred_result):
    for i in range(5):
        ret, frame = cap.read()  # 獲取當前畫面
        if not ret:
            print("無法捕捉影像")
            break
        else:
            font = cv2.FONT_HERSHEY_SIMPLEX
            datetimetext = str(datetime.datetime.now())
            frame = cv2.putText(frame, datetimetext, (10, 30), font, 1,
                                (0, 255, 255), 2, cv2.LINE_AA)
            if i == 3:
                cv2.imwrite('tmp.jpg', frame)
                pred_result = roboflow.call('tmp.jpg')
            print(pred_result)
            if pred_result != {}:
                count = 0
                for pred in pred_result['predictions']:
                    if float(pred['confidence']) > 0.7:
                        a = (int(pred['x']) - int(pred['width']/2),
                             int(pred['y']) - int(pred['height']/2))
                        b = (int(pred['x']) + int(pred['width']/2),
                             int(pred['y']) + int(pred['height']/2))
                        c = pred['confidence']
                        d = pred['class']
                        e = (int(pred['x']), int(pred['y']) - 50)
                        count += 1
                        font = cv2.FONT_HERSHEY_SIMPLEX
                        
                        frame = cv2.rectangle(frame, a, b, (0,255,0), 2)
                        frame = cv2.putText(frame, '{} {:.3}'.format(c, d),
                                            e, font, 0.5, (0, 255,255), 1)
                        
                        frame = cv2.putText(frame, f"found {count}",(10, 400), font, 1, (0, 255, 255), 2, cv2.LINE_AA)
            cv2.imshow('Camera Preview', frame)
    return pred_result

try:
    pred_result = {}
    while True:
        # 取得距離
        distance = get_distance()
        print(f"Distance: {distance} cm")
        # 若距離大於 10 公分則啟動相機預覽
        if distance > 10:
            pred_result = stream_preview(pred_result)
        
        time.sleep(1)

        # CheckSchedule.call()
        # 檢查退出條件，按 'q' 鍵退出程式
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    print("程式結束")

finally:
    cap.release()  # 釋放相機
    cv2.destroyAllWindows()  # 關閉 OpenCV 視窗
    GPIO.cleanup()  # 清理 GPIO 設定

