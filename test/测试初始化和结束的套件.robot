*** Settings ***
Suite Setup       Log    开始suite    # 获取开始执行测试套件的时间
Suite Teardown    Log    结束suit    #获取结束执行测试套件的时间
Test Setup        Log    测试案例初始化    # 测试案例初始化，目前没有输出    正在排查原因
Test Teardown     Log    测试案例结束    # 测试案例结束,目前没有输出    正在排查原因
Test Template
Test Timeout      10 seconds

*** Test Cases ***
用例初始化以及结束
    [Setup]    Log    开始setup    # 开始执行当前用例
    [Template]
    Log    我在测试初始化测试用例套件
    [Teardown]    Log    结束teardown    # 结束执行当前用例
