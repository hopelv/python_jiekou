from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.header import Header
from bs4 import BeautifulSoup
from email.utils import formataddr
import smtplib
smtp_addr='smtp.qq.com'
user='512044050@qq.com'
pwd='xofoxzeqmyjzcagc'
you='936040416@qq.com'
M=MIMEMultipart('mixed')
M['From'] = formataddr(['From俊博哥哥的关心', "me"])
M['To'] = formataddr(['关爱亲爱的宝贝', "you"])
L=[user,you]
M['Cc']=','.join(L)
d='测试发送HTML邮件'
M['Subject']=Header(d,'utf-8')


#读取HTML文件并解析发送邮件
# with open('D:\PROJECT\\test_pytest\\report\html\\123.html','r',encoding='utf-8') as f:
#     res=f.read().title()
# soup=BeautifulSoup(res,'lxml')
# h=soup.find('h').text
# # print(h)
# msg=MIMEText(h,'plain','utf-8')
# msg["Content-Disposition"] = 'attachment; filename="red_people.html"'
# M.attach(msg)


# #读取HTML文件当作文件内容发送邮件
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
# #加上下面这行代码正文将没有内容,当作附件上传
# msg["Content-Disposition"] = 'attachment; filename="red_people.html"'
# M.attach(msg)


# 发送带图片的链接
h='<html><body><img src="https://03imgmini.eastday.com/mobile/20191002/20191002173505_54408a519d79db990fbe88ac63e3c1d9_1.jpeg" alt="imageid"></body></html>'
msg=MIMEText(h,'html','utf-8')
M.attach(msg)

#加上下面这行代码实现把文本内容当作附件上传，正文将没有内容
# msg["Content-Disposition"] = 'attachment; filename="csdn.png"'




smtp=smtplib.SMTP(smtp_addr,25)
smtp.login(user,pwd)
smtp.sendmail(user,you,M.as_string())#发送邮件
smtp.quit()