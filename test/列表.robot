*** Variables ***
${kk}             10    20    30
@{u}              11    22    33    44    55

*** Test Cases ***
列表
    comment    log many    @{u}    #打印多个值
    comment    Log    ${u}    #打印一个值
    comment    Log many    ${u}    #也可以打印多个值
    ${list}    Create List    1    2    3
    ${ll}    Set Variable    a    b    c
    Log many    ${list}
    Log many    @{ll}
    @{k}    Create List    1    2    3
    @{p}    Set Variable    a    b    c
    Log many    @{k}
    Log many    @{p}
    @{lt}    Create List    x    y    z
    ${ll}    Set Variable    a    b    c
    ${t}=    Get Length    ${lt}
    ${s}=    Get Length    ${ll}
    Log    ${t}
    Log    ${s}

列表的使用
    @{argval3}    create list    abcd    WARN
    ${keyword}    set variable    log
    Run Keyword    ${keyword}    @{argval3}
