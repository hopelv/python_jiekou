*** Variables ***
${list}           1    2    3
@{litt}           4    5    6

*** Test Cases ***
输出
    Log    ${list}
    Log many    ${list}
    Log many    @{litt}
    ${s}    Set Variable    55
    Log many    ${s}
    comment    Log    @{litt}
    Log    测试    warn
