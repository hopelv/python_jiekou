*** Settings ***
Library           DateTime

*** Test Cases ***
日期处理
    ${time}    get time
    ${date}    Evaluate    datetime.datetime.now().strftime('%Y-%m-%d')    datetime
    Log    ${date}
    ${y}    Add Time To Date    ${time}    +1 day
    Log    当前日期加一天是: \ ${y}
    ${f}    Add Time To Date    ${time}    -1 day
    Log    当前日期减一天是：\ ${f}
    ${g}    Add Time To Date    ${time}    12:20:00
    Log    当前日期加时间是: \ ${g}
    ${current_time}    Get Current Date
    Log    当前时间${current_time}

对时间段操作
    ${a}    Add Time To Time    1 hour    1 minute
    Log    1小时+1分钟等于 ${a}
    ${b}    Add Time To Time    60 seconds    1 minute
    Log    ${b}
    ${c}    Add Time To Time    1 hour    30 minute    Timer    exclude_millis=yes
    Log    小时加秒并且转换格式${c}
    ${dd}    Convert Time    ${3665}    Timer    exclude)millis=yes
    Log    把${3665}转换成时间格式为${dd}

从时间中提取年月日时分秒
    ${time}    get time
    ${datetime}    Convert Date    ${time}    datetime
    Log    年：${datetime.year}
    Log    月：${datetime.month}
    Log    日：${datetime.day}
    Log    时：${datetime.hour}
    Log    分：${datetime.minute}
    Log    秒：${datetime.second}
    Log    微秒：${datetime.microsecond}

计算时间差
    ${time}    get time
    ${date}    subtract date from date    ${time}    2019-10-21 12:15:36
    Log    ${date}
    ${date1}    subtract time from date    ${time}    7 days    #必须先日期后时间
    Log    ${date1}
    ${date2}    subtract time from time    02:20:12    20    #必须是时间
    Log    ${date2}
