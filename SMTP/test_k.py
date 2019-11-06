from email.mime.multipart import MIMEMultipart#组合多个邮件对象
from email.mime.image import MIMEImage  #构造图片
from email.mime.text import MIMEText    #构造文本
from email.header import Header
import smtplib
def sendMail(you):
    user='512044050@qq.com'
    pwd='xofoxzeqmyjzcagc'
    #设置总的邮件对象
    ME=MIMEMultipart()
    #邮件头尾信息
    list=[you,'1049252083@qq.com', '936040416@qq.com']
    ME['From']=user#发件人
    ME['To']=','.join(list)#合并多个收件人
    l=['1049252083@qq.com','512044050@qq.com']
    ME['Cc']=','.join(l)#合并多个抄送人
    m='你好  杨小姐'
    #邮件主题
    ME['Subject']=Header(m,'utf-8')

    #
    #
    # 构造文本内容
    with open('D:\PROJECT\lunwen\Z公司绩效管理有效性研究.txt',encoding='utf-8') as f:
        res=f.read()
    msg=MIMEText(res,'plain','utf-8')
    #加上下面这行代码实现把文本内容当作附件上传，正文将没有内容
    # msg["Content-Disposition"] = 'attachment; filename="csdn.txt"'
    ME.attach(msg)#添加到邮件整体内容中


    # #构造图片
    # image_file = open('D:\PROJECT\picture\AL电厂经营战略分析.png', 'rb').read()
    # msg = MIMEImage(image_file)
    # msg.add_header('Content-ID', '<image1>')
    # # 如果不加下边这行代码的话，会在收件方方面显示bin文件，下载之后也不能正常打开
    # msg["Content-Disposition"] = 'attachment; filename="red_people.png"'
    # ME.attach(msg)#添加到邮件整体内容中


    #构造附件
    txt_file = open(r'D:\PROJECT\lunwen\“人性化”管理是企业管理的必然趋势.txt', 'rb').read()
    txt = MIMEText(txt_file, 'base64', 'utf-8')
    txt["Content-Type"] = 'application/octet-stream'
    #以下代码可以重命名附件为hello_world.txt发送
    txt["Content-Disposition"] = 'attachment; filename="red_people.txt"'
    ME.attach(txt)#添加到邮件整体内容中


    # #构造超文本
    # url='http://www.baidu.com'
    # html_info = """
    #     <p>点击以下链接，你会去向一个更大的世界</p>
    #     <p><a href="%s">click me</a></p>
    #     <p>i am very galsses for you</p>
    #     """% url
    # fg=MIMEText(html_info,'html','utf-8')
    # #加上下面这行代码实现把文本内容当作附件上传，正文将没有内容
    # fg["Content-Disposition"] = 'attachment; filename="csdn.html"'
    # ME.attach(fg)#添加到邮件整体内容中

    flage=True
    while flage:
        try:
            smp=smtplib.SMTP('smtp.qq.com',25)
            smp.login(user,pwd)
            smp.sendmail(user,you,ME.as_string())
            print('邮件发送成功')
            break
        except:
            print('邮件发送失败，尝试重新发送')
            break
if __name__=='__main__':
    sendMail('936040416@qq.com')