*** Test Cases ***
连接元素
    ${str}    Catenate    hello    world
    Log    ${str}
    ${str2}    Catenate    SEPARATOR=--    hello    world
    Log    ${str2}
