#!/usr/bin/env python3

import smtplib
from email.mime.text import MIMEText

user = 'dmmjy9@live.cn'
def mail(user):
    ret = True
    try:
        msg = MIMEText('邮件内容','plain','utf-8')
        msg['From'] = 'dmmjy9_send'
        msg['To'] = 'dmmjy9_receive'
        msg['Subject'] = '主题'

        server = smtplib.SMTP('smtp.163.com',25)
        server.login('dmmjy9@163.com','0830--Mjy')
        server.sendmail('dmmjy9@163.com',[user,],msg.as_string())
        server.quit()
    except Exception as e:
        print (e)
        ret = False
    return ret

ret = mail(user)
if ret:
    print("Succeed")
else:
    print("Failed")