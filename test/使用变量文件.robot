*** Settings ***
Variables         ../../testvariable.py
Variables         ../../tty.py
Variables         ../../uvw.py

*** Test Cases ***
使用变量文件
    Log    开始执行时间：${startime}
    Log    ${MAPPING}
    Log    ${name}
    Log    ${end}
    Log    结束执行时间：${endtime}
    Log    ${name}
    Log    ${phone1}
    Log To Console    ${phone1}    #使用cmd窗口会打印出来
