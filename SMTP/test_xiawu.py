import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
def send_mail(you):
    smtp_addr='smtp.qq.com'
    me='512044050@qq.com'
    pwd='xofoxzeqmyjzcagc'
    h='<html><body><h1>亲爱的宝贝：<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;下班喽，老公在家里等你哦，注意安全！！<h1><img src="http://pic18.nipic.com/20120111/9023494_111902422000_2.jpg"" alt="imageid"></body></html>'
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
        print('发送邮件成功')
    except:
        print('发送邮件失败')
if __name__=='__main__':
    you='1049252083@qq.com'
    send_mail(you)