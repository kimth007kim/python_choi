import smtplib
from email.mime.text import MIMEText

me= 'kimth007kim@gmail.com'
you = 'kimth007kim@naver.com'
contents='12월 20일에 동창회가 있으니 참석해주기 바랍니다.'

msg= MIMEText(contents, _charset='euc-kr')
msg['Subject']= '동창회 모임'
msg['From']= me
msg['To']= you

server = smtplib.SMTP('kimth007kim@gmail.com',587)
server.ehlo()
server.starttls()
server.ehlo()

server.login("자신의 아이디","패스워드")

server.sendmail(me,you,msg.as_string())
server.quit()