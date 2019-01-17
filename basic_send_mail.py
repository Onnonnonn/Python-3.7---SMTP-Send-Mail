"""
author : Onnonnonn
date : 01/17/2019
"""
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP
import email.utils
import smtplib
import sys
 
sender = 'sender mail address'# 寄件者的信箱 , 同時用於登入
passwd = 'password to login sending mail server EX:gmail , yahoo .....'# 寄件信箱登入用的密碼 , 要允許使用使用登入方式較不安全的應用程式
receiver = "receiver's mail address"# 收件者的信箱

msg = MIMEMultipart(_subtype='related')
msg['Date'] = email.utils.formatdate()# 信件日期
msg['From'] = "Sender's nickname <"+sender+">"# 寄件者的別稱 <寄件者的信箱>
#msg['From'] = sender
msg['To'] = receiver # 收件者的信箱
msg['Message-ID'] = email.utils.make_msgid()# 信件編號
msg['Subject'] = "Title"# 信件標題

mail_msg='''input your message here'''# 信件內容
part = MIMEText(mail_msg,_charset='utf-8') # 使用MIME格式
msg.attach(part)# 加入信件

try:
	smtp = smtplib.SMTP("smtp_mail_server:port")# 設定寄件信箱的SMTP server位置和port(上網查)
	smtp.ehlo()
	smtp.starttls()
	smtp.login(sender, passwd)# 登入
	smtp.sendmail(sender, receiver , msg.as_string())# 寄出信件
	print(msg.as_string()) # 印出完整信件內容
except smtplib.SMTPException as err:
	print("Error: ",err)