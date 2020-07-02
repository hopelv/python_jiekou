*** Test Cases ***
时间的操作
    ${time}    get time    #获取当前时间
    Log    ${time}
    ${yyyy}    ${mm}    ${dd}    ${hh}    ${min}    ${ss}    get time    year,month,day,hour,minute,second
    sleep    5    #休眠5秒
    Log many    ${yyyy}-${mm}-${dd} \ ${hh}:${min}:${ss}
    ${s}    get time    epoch
    Log    当前时间的字符串格式${s}
