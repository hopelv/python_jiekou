*** Test Cases ***
evaluate
    ${num}    evaluate    random.randint(1,100)    random    #执行python的方法
    Log    第一次打印 \ ${num}
    import library    d:/test.py
    ${data}    int    ${num}    #调用编写的python脚本
    Log    第二次打印 \ ${data}
    ${data}    evaluate    int(${num})    #调用编写的python脚本
    Log    第三次打印 \ ${data}
