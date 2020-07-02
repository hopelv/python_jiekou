*** Test Cases ***
判断变量赋值
    ${num}    Set variable    ${100}    ${200}    ${300}
    FOR    ${i}    IN    @{num}
        ${j}    Set Variable if    ${i} < ${200}    条件成立    条件不成立    #因为只有小于200，所以输出：条件成立 条件不成立 条件不成立
    END
