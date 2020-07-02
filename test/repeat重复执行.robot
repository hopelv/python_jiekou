*** Settings ***
Library           Screenshot

*** Test Cases ***
repeat
    repeat keyword    1    Log    a
    Repeat Keyword    2    Log    b

截图
    Take screenshot
