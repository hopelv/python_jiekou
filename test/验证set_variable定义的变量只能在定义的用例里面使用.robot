*** Settings ***
Resource          resource资源文件.robot

*** Test Cases ***
验证1
    ${num}    set variable    200
    Log    ${num}

验证2
    comment    Log    ${num}    #不能输出 因为num是在【验证1】定义的

验证loca
    @{m}    set variable    88    99    100
    FOR    ${i}    IN    @{m}
        set local variable    ${m}    local变量
        Log    ${i}    #88,99,100
        Log    ${m}    #输出local变量,覆盖了 88 99 100
    END
    Log    ${m}    #输出local变量，,覆盖了 88 99 100

打印默认值
    百度    99    #输出默认参数
    百度    88    88    #不打印默认参数

打印默认值列表字典
    @{ls}    Create List    10    20    30
    &{dicts}    Create Dictionary    num1=100    num2=200    num3=300
    默认值&列表    1    2    ${:}    @{ls}    &{dicts}
