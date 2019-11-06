from email.mime.text import MIMEText
import smtplib
from email.utils import formataddr
def send_mail(you):
    smtp_addr='smtp.qq.com'
    me='512044050@qq.com'
    pwd='xofoxzeqmyjzcagc'

    h='<html><body><h1>亲爱的宝贝：<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;辛苦一个上午了,再忙也要记得吃饭哦！！<h1><img src="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1570271151549&di=f9ae5b37c25836e7b0caea7415a634b8&imgtype=0&src=http%3A%2F%2Fcp2.douguo.net%2Fupload%2Fcaiku%2F3%2F5%2F1%2Fyuan_35795354409dfbecd7a7a5497cfc56f1.jpg" alt="imageid"></body></html>'
    msg=MIMEText(h,'html','utf-8')
    msg['From'] = formataddr(['From俊博哥哥的关心', "me"])
    msg['To'] = formataddr(['亲爱的宝贝', "you"])
    L=[me,you]
    msg['Cc']=','.join(L)
    msg['Subject']='爱的呼唤'
    try:
        smtp=smtplib.SMTP(smtp_addr,25)
        smtp.login(me,pwd)
        smtp.sendmail(me,you,msg.as_string())
        smtp.quit()
        print('邮件发送成功')

    except:
        print('邮件发送失败')

if __name__=='__main__':
    you='1049252083@qq.com'
    send_mail(you)
