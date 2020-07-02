*** Settings ***
Library           Collections

*** Test Cases ***
字典
    ${dict1}    Create Dictionary    num    2    name    刘备
    ${dict2}    Create Dictionary    add    深圳    age    ${18}
    Log    ${dict1}    #默认打印字典所有元素
    Log    ${dict2}    #默认打印字典所有元素
    ${item1}    get dictionary items    ${dict1}    #获取dict1所有元素
    ${item2}    get dictionary items    ${dict2}    #获取dict1所有元素
    Log    ${item1}
    Log    ${item2}
    ${key1}    get dictionary keys    ${dict1}    #获取dict1的所有键
    ${key2}    get dictionary keys    ${dict2}    #获取dict2的所有键
    Log    ${key1}
    Log    ${key2}
    ${value1}    get dictionary values    ${dict1}    #获取dict1的所有值
    ${value2}    get dictionary values    ${dict2}    #获取dict1的所有值
    Log    ${value1}
    Log    ${value2}
    ${s}    get from dictionary    ${dict1}    name
    Log    ${s}
