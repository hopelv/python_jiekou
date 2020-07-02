*** Test Cases ***
列表元素的使用
    ${list}    Create List    10    20    30    40    50
    Log    第一次\${list}[1]输出列表的第二个值: ${list}[1]
    Log    第二次\${list[1]}输出列表的第二个值: ${list[1]}
