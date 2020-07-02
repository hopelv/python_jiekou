*** Settings ***
Documentation     第一个测试的例子
Library           Selenium2Library    # selenium UI自动化库
Library           Screenshot    # 截图模块
Library           MyRobotFwkLib

*** Variables ***
${num}            55
@{list}           11    33    44    55

*** Test Cases ***
log
    [Documentation]    这是一个案例
    Log    "测试"
    Log    "你在干嘛"
    comment    Open Browser    http://www.baidu.com    chrome
    ${num}    Set variable    55
    Log    ${num}
    @{s}    Create List    a    b    c
    Log many    @{s}
    ${time}    get time
    Log    ${time}
    ${yyyy}    ${mm}    ${dd}    get time    year,month,day
    Log    ${yyyy}
    Log    ${mm}
    Log    ${dd}
    Log    ${yyyy}-${mm}-${dd}
    Take screenshot
    Log many    @{list}
    evaluate    "helloworld"
    ${curre_time}    get_current_time
    Log    ${curre_time}

注释
    comment    这是一个注释不会输出
    Log    我不是注释所以会输出    #我不会被输出
