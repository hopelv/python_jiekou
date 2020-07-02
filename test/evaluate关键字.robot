*** Settings ***
Documentation     *关键字加粗*

*** Variables ***
${kk}             10    20    30
@{u}              11    22    33    44    55

*** Test Cases ***
evaluate
    [Documentation]    _测试用例斜体_
    [Template]
    ${num}    evaluate    random.randint(1,200)    random
    import library    d:/test.py
    ${newNum}    evaluate    int(${num})
    ${newTwoNum}    evaluate    int(200)
