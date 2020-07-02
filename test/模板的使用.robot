*** Settings ***
Suite Setup

*** Test Cases ***
使用模板
    [Template]    模板
    99    55    88
    77    66    444

*** Keywords ***
模板
    [Arguments]    @{name}
    @{list}    create list    @{name}
    FOR    ${i}    IN    @{list}
        Log    ${i}
    END
