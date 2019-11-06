import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
def send_mail(you):
    smtp_addr='smtp.qq.com'
    me='512044050@qq.com'
    pwd='xofoxzeqmyjzcagc'

    h='<html><body><h1>亲爱的宝贝：<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;夜深了,该睡美容觉喽！！<h1><img src="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1570273231533&di=d95fbd59e32a8dbcc8ba8d267e06abb1&imgtype=0&src=http%3A%2F%2Fbmp.skxox.com%2F201612%2F27%2Fmy18800541960.135015.jpg" alt="imageid"></body></html>'
    msg=MIMEText(h,'html','utf-8')
    msg['Subject']='爱的呼唤'
    msg['From'] = formataddr(['From俊博哥哥的关心', "me"])
    msg['To'] = formataddr(['亲爱的宝贝', "you"])
    L=[me,you]
    msg['Cc']=','.join(L)

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