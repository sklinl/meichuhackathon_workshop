import uvicorn
from fastapi import FastAPI
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import base64
from email.mime.image import MIMEImage
from pathlib import Path
from fastapi import File, UploadFile
import numpy as np
# import model.detection as det
import cv2 as cv
import time


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


@app.post('/api/v2/alert')
def post_image(file: bytes = File(...), recipients: str = 'kevinlinsk19@gmail.com'):


    content = MIMEMultipart()  #建立MIMEMultipart物件
    content["subject"] = "[ALARM] Please check it for more detail"  #郵件標題
    content["from"] = "kevinlinsk19@gmail.com"  #寄件者
    content["to"] = (', ').join(recipients.split(',')) #收件者
    content.attach(MIMEText("你違規了來自上傳的檔案"))  #郵件內容
    content.attach(MIMEImage(file))  # 郵件圖片內容
    print("attach file success.")
    with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:  # 設定SMTP伺服器

        try:
            smtp.ehlo()  # 驗證SMTP伺服器
            smtp.starttls()  # 建立加密傳輸
            smtp.login("kevinlinsk19@gmail.com", gmail_token)  # 登入寄件者gmail
            smtp.send_message(content)  # 寄送郵件

            print("Complete!")

        except Exception as e:
            print("Error message: ", e)

    time.sleep(3)

    return 'OK'

@app.post('/api/v3/alert')
async def post_image(file: UploadFile = File(...), recipients: str = 'kevinlinsk19@gmail.com'):

    contents = await file.read()
    nparr = np.fromstring(contents, np.uint8)
    img = cv.imdecode(nparr, cv.IMREAD_COLOR)
    # result = det.predict(img)


    content = MIMEMultipart()  #建立MIMEMultipart物件
    content["subject"] = "[ALARM] Please check it for more detail"  #郵件標題
    content["from"] = "kevinlinsk19@gmail.com"  #寄件者
    content["to"] = (', ').join(recipients.split(',')) #收件者
    content.attach(MIMEText("你違規了來自AI"))  #郵件內容
    # content.attach(MIMEImage(result))  # 郵件圖片內容
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
