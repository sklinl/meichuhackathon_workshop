import uvicorn
from fastapi import FastAPI
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import base64


app = FastAPI(title='AI Alert sender')
gmail_token = base64.b64decode("d3doem92YXlzY2VzenJ5aw==").decode('utf-8')

@app.get('/api/v1/alert')
def send_email(recipients: str = 'kevinlinsk19@gmail.com'):


    content = MIMEMultipart()  #建立MIMEMultipart物件
    content["subject"] = "[ALARM] Please check it for more detail"  #郵件標題
    content["from"] = "kevinlinsk19@gmail.com"  #寄件者
    content["to"] = (', ').join(recipients.split(',')) #收件者
    content.attach(MIMEText("你違規了"))  #郵件內容

    with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:  # 設定SMTP伺服器
        try:
            smtp.ehlo()  # 驗證SMTP伺服器
            smtp.starttls()  # 建立加密傳輸
            smtp.login("kevinlinsk19@gmail.com", gmail_token)  # 登入寄件者gmail
            smtp.send_message(content)  # 寄送郵件

            print("Complete!")

        except Exception as e:
            print("Error message: ", e)

    return 'OK'

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
