*** Settings ***

*** Keywords ***
搜索
    [Arguments]    ${num1}    ${num2}
    Log    ${num1} ${num2}

百度
    [Arguments]    ${num1}    ${num2}=100
    Log    ${num1}
    Log    ${num2}

默认值&列表
    [Arguments]    ${a}    ${b}    ${c}=我是c    @{lists}    &{dicts}
    Log    第一个参数a的内容是 \ \ ${a}
    Log    第二个参数b的内容是 \ \ ${b}
    Log    第三个默认值的内容是 \ \ ${c}
    Log    第四个参数【lists】的内容是 \ \ @{lists}
    Log    最后一个参数【dicts】是 \ \ &{dicts}

返回列表
    [Arguments]    @{lists}
    FOR    ${s}    IN    @{lists}
        Log    ${s}
    END
    [Return]    ${lists}    #前面可以写@、 $ 不影响接收的格式,但是不能写& 会报错

返回字典
    [Arguments]    &{dicts}
    FOR    ${key}    IN    ${dicts}
        Log    ${key}
    END
    [Return]    ${dicts}    #前面@输出键 $输出字典    @输出键值对

单个返回值
    [Arguments]    ${yh}
    [Return]    我是返回的单个变量${yh}
