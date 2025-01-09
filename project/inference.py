import requests
import cv2

class Roboflow:
    def __init__(self):
        # 設定 API 金鑰和模型資訊
        self.api_key = "tyljdBoYNEv8iHY9HY5J" 
        self.model_id = "medicine-jar" 
        self.model_version = "1" # 模型版本號
        # 設定推論端點 URL
        self.inference_url = f"https://outline.roboflow.com/{self.model_id}/{self.model_version}?api_key={self.api_key}" 
    def call(self, image_path: str):
        try:
            # 讀取圖片並進行推論
            with open(image_path, "rb") as image_file: 
                response = requests.post(self.inference_url, files={"file": image_file})
                # 處理回傳結果
                if response.status_code == 200: 
                    result = response.json() 
                    print("推論結果：", result)
                    return result 
                else: 
                    print("錯誤：", response.status_code, response.text) 
                    return None
        except Exception as e: 
            print("發生例外錯誤：", str(e)) 
            return None

roboflow_instance = Roboflow()
image_path = "preview.jpg"
result = roboflow_instance.call(image_path)
image = cv2.imread(image_path)
for pred in result['predictions']:
    a = (int(pred['x']) - int(pred['width']/2), int(pred['y']) - int(pred['height']/2))
    b = (int(pred['x']) + int(pred['width']/2), int(pred['y']) + int(pred['height']/2))
    c = pred['confidence']
    d = pred['class']
    e = (int(pred['x']), int(pred['y']) - 50)
    font = cv2.FONT_HERSHEY_SIMPLEX
    
    image = cv2.rectangle(image, a, b, (0,255,0), 2)
    image = cv2.putText(image, '{} {:.3}'.format(c, d), e, font, 0.5, (0, 255,255), 1)
    
cv2.imwrite('result.jpg', image)