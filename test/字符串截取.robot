*** Test Cases ***
字符串截取
    ${str}    set variable    hello,world
    Log    ${str[:8]}
    Log    ${str[2:8]}
    Log    ${str[:]}
