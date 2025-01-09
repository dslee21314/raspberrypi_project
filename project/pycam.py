import RPi.GPIO as GPIO
import time
from datetime import datetime
from picamera import PiCamera
import cv2

#pir = 18
#led_green = 23
#camera = PiCamera()

#GPIO.setmode(GPIO.BCM)
#GPIO.setup(pir, GPIO.IN)

# now = datetime.now()
# ptime = now.strftime("%Y_%m_%d_%H%M%S")
# camera.capture('./picamera/image_%s.jpg' % ptime)
# camera.stop_preview()

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, -1)
    
    cv2.imshow('frame', frame)
    
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    
cap.release()
cv2.destroyAllWindows()

#while True:
#    input_state = GPIO.input(pir)
#    if input_state == True:
#        print('Motion Detected')
#        GPIO.setup(led_green, GPIO.OUT)
#        now = datetime.now()
#        ptime = now.strftime("%Y_%m_%d_%H%M%S")
#        camera.capture('/home/pi/image_%s.jpg' % ptime)
#        print('A photo has been taken')
#        time.sleep(10)
#    else:
#        GPIO.setup(led_green, GPIO.IN)
#        camera.stop_preview()
