*** Test Cases ***
If判断单条件输出
    ${Score}    Set Variable    90
    Run Keyword if    ${Score}>=90    Log    "优秀"
    ...    ELSE IF    ${Score}>=80    Log    "良好"
    ...    ELSE IF    ${Score}>=60    Log    "及格"
    ...    ELSE    Log    "不及格"

if判断多条件输出
    ${addrs}    Set Variable    深圳    北京    上海    西安    广东    陕西人民政府
    FOR    ${addr}    IN    @{addrs}
        ${addrlength}    Get length    ${addr}
        Run Keyword if    '${addr}'=='深圳' or '${addr}'=='北京'    Log    我在深圳or北京
        ...    ELSE IF    '${addr}'=='上海' or '${addr}'=='西安'    Log    我在上海or西安
        ...    ELSE IF    ${addrlength} > ${2}    Log    100
        ...    ELSE    Log    我不知道你在那里
    END
