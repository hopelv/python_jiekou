import os,unittest,time,HTMLTestRunner
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr
from email.header import Header
cur_path=os.path.dirname(os.path.realpath(__file__))#获取当前文件的目录
print('当前目录',cur_path)


# 1.cur_path这个参数是读取当前这个脚本的真实路径，也就是run_main.py的真实路径
# 2.caseName="case"这个case是存放测试用例的文件夹，如果没有的话，自动创建。如果想运行其它文件夹的用例，就改下caseName这个参数值
# 3.rule="test*.py"这个是匹配用例脚本名称的规则，默认匹配test开头的所有用例
def add_case(caseName="case",rule="test_*.py"):
    '''第一步加载所有的测试用例'''
    case_path=os.path.join(cur_path,caseName)#获取的是用例文件夹
    #如果不存case文件夹就创建一个
    if not os.path.exists(case_path):
        os.mkdir(case_path)
    print("测试用例文件夹:{}".format(case_path))
    #定义discover方法的参数,获取测试文件下面所有的测试方法
    discover=unittest.defaultTestLoader.discover(case_path,pattern=rule,top_level_dir=None)
    print(discover)
    return discover



# 1.把上一步加载到用例的参数传入这个函数，测试报告的文件名称默认report文件夹：reportName="report
# 2.如果没有这个report文件夹也没关系，可以自动创建的def run_case(all_case,reposrName='report'):

def run_case(all_case,reportName="report"):
    '''执行所有用例，把结果写入HTML 报告中'''
    now=time.strftime('%Y-%m-%d-%H-%M-%S')
    report_path=os.path.join(cur_path,reportName)#测试报告文件夹
    if not os.path.exists(report_path):
        os.mkdir(report_path)
    report_abspath=os.path.join(report_path,now+'result.html')
    print('测试报告文件夹：%s'%report_abspath)
    with open(report_abspath,'wb') as f:
        runner=HTMLTestRunner.HTMLTestRunner(stream=f,title=u'自动化测试报告,测试结果如下：',description=u'用例执行情况')

        #调用add_case函数返回值
        runner.run(all_case)





def get_report_file(report_path):
    '''获取最新的测试报告'''
    lists=os.listdir(report_path)
    lists.sort(key=lambda fn:os.path.getmtime(os.path.join(report_path,fn)))
    print('最新生成的测试报告',lists[-1])
    report_file=os.path.join(report_path,lists[-1])
    return report_file



# 第四步：发送测试报告到邮箱
# 1.像QQ邮箱这种ssl加密的就走SMTP_SSL，用授权码登录

# 2.其它邮箱就正常账号密码登录，走SMTP

def send_mail(sender,psw,receiver,smtpserver,report_file,port):
    '''第四步，发送最新的测试报告内容'''
    with open(report_file,'rb') as f:
        mail_body=f.read()
        # print(mail_body)
        #定义邮件内容
        msg=MIMEMultipart()
        body=MIMEText(mail_body,_subtype='html',_charset='utf-8')
        m=u'自动化测试报告'
        msg['subject']=Header(m,'utf-8')
        msg['from']=sender
        msg['to']=receiver
        msg.attach(body)
        #添加附件
        att=MIMEText(open(report_file,'rb').read(),'base64','utf-8')
        att['Content-Type']='application/octet-stream'
        att['Content-Disposition']='attachment;filename="report.html"'
        msg.attach(att)

        try:
            smp = smtplib.SMTP(smtpserver,port)
            smp.login(sender,psw)
            smp.sendmail(sender,receiver,msg.as_string())
            print('发送邮件成功')
        except:
            print('发送邮件失败')

if __name__=='__main__':
        all_case=add_case()#加载用例
        #生成测试报告的路径
        run_case(all_case)
        #获取最新的测试报告文件
        report_path=os.path.join(cur_path,'report')#用例文件夹
        report_file=get_report_file(report_path)#获取最新的测试报告文件
        #导入config文件，获取读取配置文件的信息
        from hope_jiegou.config.readConfig import read_config

        # smtp服务器,邮件服务器端口,授权码，发件人，收件人
        smtpserver, port, psw, sender, receiver = read_config()
        # print(type(sender),type(psw),type(smtpserver),type(port),type(receiver))
        # 发送报告
        send_mail(sender,psw,receiver,smtpserver,report_file,port)