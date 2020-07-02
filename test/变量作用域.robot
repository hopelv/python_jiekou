*** Settings ***
Library           DateTime

*** Variables ***

*** Test Cases ***
设置变量作用域
    #第一个用例
    ${localname}    Set variable    100
    Set Global Variable    ${globalname}    我是设置的global变量
    Set local Variable    ${localname}    我是设置的lobal变量    #覆盖了100
    Set suite Variable    ${suitename}    我是设置的suite变量
    Set Test Variable    ${casename}    我是设置的case变量
    Log    ${localname}·    #输出 ：我是设置的lobal变量,因为后面设置的local变量的值覆盖了之前的100

使用设置的变量作用域
    #第二个用例
    Log    ${globalname}    #输出：我是设置的global变量
    Log    ${suitename}    #输出： 我是设置的suite变量
    #Log    ${localname}    #输出报错，因为local变量只能在定义的用例里面打印
    Log    ${testname}    #输出报错，因为test只能在定义的用例里面打印

打印环境变量
    #第三个用例
    Log    %{PATH}    #打印path的内容
