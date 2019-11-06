import smtplib
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
from email.utils import formataddr
def send_mail(you):
    smtp_addr='smtp.qq.com'
    me='512044050@qq.com'
    pwd='xofoxzeqmyjzcagc'

    # # #读取HTML文件当作文件内容发送邮件
    # with open('D:\PROJECT\\test_pytest\\report\html\Selenium2Library.html') as f:
    #     res=f.read()
    # # print(res)
    # soup=BeautifulSoup(res,'lxml')
    # b=soup.find('body')
    # div=b.find('div')
    # result=[]
    # h=div.find('h1').text
    # result.append(h+'\n')
    # li_list=div.find_all('li')
    # for  li in li_list:
    #     result.append(li.text+'\n')
    # ret=''.join(result)
    # msg=MIMEText(ret,'plain','utf-8')
    # #同时当作附件上传
    # msg["Content-Disposition"] = 'attachment; filename="red_people.html"'
    h='<html><body><h1>亲爱的宝贝：<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;早上好,起床喽，记得吃早餐哦！！<h1><img src="http://img.mp.itc.cn/upload/20170115/e2b9f37aac11403d8458e90b2c67497b_th.jpg" alt="imageid"></body></html>'
    msg=MIMEText(h,'html','utf-8')
    msg['Subject']='爱的呼换'
    L=[me,you]
    msg['From'] = formataddr(['From俊博哥哥的关心', "me"])
    msg['To'] = formataddr(['亲爱的宝贝', "you"])
    msg['Cc'] = ','.join(L)

    try:
        smtp=smtplib.SMTP(smtp_addr,25)
        smtp.login(me,pwd)
        smtp.sendmail(me,you,msg.as_string())
        smtp.quit()
        print('发送邮件成功')
    except:
        print('发送邮件失败')

if __name__=="__main__":
    you='1049252083@qq.com'
    send_mail(you)