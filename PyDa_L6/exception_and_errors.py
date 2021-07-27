'''
Задание 1
Печатные газеты использовали свой формат дат для каждого выпуска.
Для каждой газеты из списка напишите формат указанной даты
для перевода в объект datetime:
The Moscow Times - Wednesday, October 2, 2002
The Guardian - Friday, 11.10.13
Daily News - Thursday, 18 August 1977
'''

from datetime import datetime

the_moscow_times = 'Friday, 11.10.13'
the_guardian = 'Friday, 11.10.13'
daily_news = 'Thursday, 18 August 1977'

print(datetime.strptime(the_moscow_times, '%A, %d.%m.%y'))
print(datetime.strptime(the_guardian, '%A, %m.%d.%y'))
print(datetime.strptime(daily_news, '%A, %d %B %Y'))

'''
Задание 2
Дан поток дат в формате YYYY-MM-DD, в которых встречаются некорректные значения:
stream = [‘2018-04-02’, ‘2018-02-29’, ‘2018-19-02’]
Напишите функцию, которая проверяет эти даты на корректность.
Т. е. для каждой даты возвращает True (дата корректна)
или False (некорректная дата).
'''

from datetime import datetime

stream = ['2018-04-02', '2018-02-29', '2018-19-02']
for d in stream:
    try:
        datetime.strptime(d, '%Y-%m-%d')
    except:
        print(d, 'False (некорректная дата)')
    else:
        print(d,'True (дата корректна)')
'''
Задание 3
Напишите функцию date_range, которая возвращает список дат за период
от start_date до end_date. Даты должны вводиться в формате YYYY-MM-DD.
В случае неверного формата или при start_date > end_date должен
возвращаться пустой список.
'''
from datetime import datetime
from datetime import timedelta

start_date = input('Введите дату в формате YYYY-MM-DD: ')
end_date = input('Введите дату в формате YYYY-MM-DD: ')

def date_true_(s_d, e_d):
    flag = True
    try:
        datetime.strptime(s_d, '%Y-%m-%d')
    except:
        flag = False
        error_s = 'False (некорректная первая дата)'
        print(error_s)

    try:
        datetime.strptime(e_d, '%Y-%m-%d')
    except:
        flag = False
        error_s = 'False (некорректная вторая дата)'
        print(error_s)
    return flag

def date_range(s_d, e_d):
    list_date = []
    f = date_true_(s_d, e_d)
    if  f == True and s_d < e_d:
        start = datetime.strptime(s_d, '%Y-%m-%d')
        finish = datetime.strptime(e_d, '%Y-%m-%d')
        tts = start.timetuple()[7]
        ttf = finish.timetuple()[7]
        for d in range(ttf - tts + 1):
            list_date.append((start + timedelta(days = d)).strftime('%Y-%m-%d'))
    elif f == False or s_d > e_d:
        return list_date
    return list_date

def date_range_2(s_d, e_d):
    start_date_dt = datetime.strptime(s_d, '%Y-%m-%d')
    end_date_dt = datetime.strptime(e_d, '%Y-%m-%d')
    list_date = []
    f = date_true_(s_d, e_d)
    if  f == True and s_d < e_d:
        while start_date_dt <= end_date_dt:
            list_date.append(start_date_dt.strftime('%Y-%m-%d'))
            start_date_dt += timedelta(days=1)
    elif f == False or s_d > e_d:
        return list_date
    return list_date

print(*date_range(start_date, end_date))
print(date_range_2(start_date, end_date))
