import requests

class LineNotify:
    def __init__(self, token):
        """
        初始化 LineNotify 物件，必須傳入 LINE Notify 的 token。
        :param token: LINE Notify 的存取 token
        """
        self.token = token
        self.api_url = "https://notify-api.line.me/api/notify"
    
    def send_message(self, message):
        """
        發送訊息到 LINE 群組或個人
        :param message: 需要發送的訊息文字
        :return: 回應的 JSON 格式內容
        """
        headers = {
            'Authorization': f'Bearer {self.token}'
        }
        data = {
            'message': message
        }
        
        response = requests.post(self.api_url, headers=headers, data=data)
        
        # 回傳發送結果
        if response.status_code == 200:
            return {"status": "success", "message": response.json()}
        else:
            return {"status": "error", "message": response.text}
    

# 使用範例：
if __name__ == "__main__":
    # 請替換成你的 LINE Notify token
    line_token = 'YOUR_LINE_NOTIFY_TOKEN'
    
    # 建立 LineNotify 物件
    notifier = LineNotify(line_token)
    
    # 發送訊息
    result = notifier.send_message("這是一個測試訊息！")
    
    print(result)

