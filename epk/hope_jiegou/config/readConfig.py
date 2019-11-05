import  configparser
import os
def read_config():
    ads_path=os.path.abspath(__file__)#当前文文件目录路径
    curr_path=os.path.dirname(ads_path)#当前文件所在的目录
    # print(ads_path)
    # print(curr_path)
    file_path=os.path.join(curr_path,'cfg.ini')
    cfg=configparser.ConfigParser()
    cfg.read(file_path)
    smtpServer=cfg.get('email','smtpserver')
    port=cfg.getint('email','port')
    psw=cfg.get('email','psw')
    sender=cfg.get('email','sender')
    receiver=cfg.get('email','receiver')
    return smtpServer,port,psw,sender,receiver

    # print(smtpServer,port,psw,sender,receiver)