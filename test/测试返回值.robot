*** Settings ***
Resource          resource资源文件.robot

*** Test Cases ***
测试列表返回值
    @{g}    返回列表    11    12    13
    Log many    @{g}
    Log many    ${g}

测试字典返回值
    &{d}    返回字典    a=88    b=99    c=100
    Log many    ${d}    #$打印的是整个字典，&打印的是单个键值对
    Log many    &{d}    #$打印的是整个字典，&打印的是单个键值对
    Log many    @{d}    #$打印的是键

测试单个返回值
    ${f}    单个返回值    200
    Log    ${f}
