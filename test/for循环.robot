*** Test Cases ***
for循环
    FOR    ${i}    IN RANGE    5    10    2
        Log    ${i}    #输出5,7,9
    END
    ${abc}    Create List    a    b    c
    FOR    ${i}    IN    @{abc}
        run keyword if    '${i}'=='b'    continue for loop    #条件为true跳过当前循环
        Log    ${i}    #输出a,c 跳过b
    END
    FOR    ${t}    IN    @{abc}
        exit for loop if    '${t}'=='b'    #条件为true,结束循环
        Log    ${t}
    END
    FOR    ${f}    IN    @{abc}
        Run keyword if    '${f}'=='b'    exit for loop
        Log    ${f}
    END

for in enumerate获取索引
    @{list}    create list    a    b    c    d
    FOR    ${index}    ${lt}    IN ENUMERATE    @{list}
        Log    ${lt}的索引是${index}
    END

FOR in zip循环多个列表
    ${ages}    create list    10    20    30
    ${names}    create list    张三    李四    王麻子
    FOR    ${name}    ${age}    IN ZIP    ${names}    ${ages}
        Log    ${name} \ 年龄 \ ${age}
    END

FOR in zip循环多个字典
    ${dict1}    create dictionary    张三    50    李四    49
    ${dict2}    create dictionary    刘备    78    诸葛亮    99
    FOR    ${dt}    ${dict}    IN ZIP    ${dict1}    ${dict2}
        Log    ${dt}${dict}
    END
