*** Test Cases ***
多维数组
    ${list1}    Create List    10    20    30
    ${list2}    Create List    40    50    60
    ${list3}    Create List    ${list1}    ${list2}    #输出的是二维数组
    ${list4}    Create List    @{list1}    @{list2}    #输出的是一维数组，因为使用的是@
    ${list5}    Create List    ${list3}    ${list4}    #输出的是三维数数组
    Log    ${list3}
    Log    ${list4}
    Log    ${list5}
    Log    ${list5}[0][0][1]    #输出20
    Log    ${list5[0][0][1]}    #输出20
