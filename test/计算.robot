*** Test Cases ***
计算
    ${num}    set variable    100
    ${sum}    evaluate    ${num}+100    #加
    Log    ${num}+100等于${sum}
    ${result}    evaluate    ${num}*100    #乘
    Log    ${num}乘以100等于${result}
    ${m}    evaluate    ${num}//100    #取余
    Log    ${num} 整除 100 等于${m}
    ${t}    evaluate    ${num}/20    #除
    Log    ${num}除以20等于${t}
    ${b}    evaluate    ${num}**5    #次方
    Log    ${num} 5 次方等于${b}
    Log    1+9
