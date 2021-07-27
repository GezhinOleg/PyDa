'''
Дана переменная, в которой хранится слово из латинских букв.
Напишите код, который выводит на экран:
    среднюю букву, если число букв в слове нечетное;
    две средних буквы, если число букв четное.
'''
# word = input()
# slise = int(len(word)/2)
#
# if len(word) % 2 == 0:
#     slise2 = slise-1
#     print(word[slise2], word[slise])
# else:
#     print(word[slise])

# '''
# Напишите программу, которая последовательно запрашивает у пользователя числа
# (по одному за раз) и после первого нуля выводит сумму всех ранее введенных
# чисел.
# '''
#
# num = int(input('Введите целое число и нажмите "Enter:" '))
# sum = 0
#
# while num != 0:
#     sum += num
#     num = int(input('Введите ещё целое число и нажмите "Enter:" '))
# else:
#     print('Сумма введеных чисел: 'sum)


# boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
# girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
#
# if len(boys) == len(girls):
#     for i, j in zip(sorted(boys), sorted(girls)):
#     	print(i, j, sep = ' и ')
# else:
#     print('Внимание, кто-то может остаться без пары!')
# '''
# У нас есть список, содержащий информацию о среднедневной температуре
# в Фаренгейтах за произвольный период по странам (структура данных в примере).
# Необходимо написать код, который рассчитает среднюю температуру за период
# в Цельсиях(!) для каждой страны.
# '''
# countries_temperature = [
#     ['Thailand', [75.2, 77, 78.8, 73.4, 68, 75.2, 77]],
#     ['Germany', [57.2, 55.4, 59, 59, 53.6]],
#     ['Russia', [35.6, 37.4, 39.2, 41, 42.8, 39.2, 35.6]],
#     ['Poland', [50, 50, 53.6, 57.2, 55.4, 55.4]]
# ]
# print('Средняя температура в странах:')
# for i in countries_temperature:
#     t_fahrenheit = sum(i[1])/len(i[1])
#     t_celsius = round(5/9 * (t_fahrenheit - 32), 1)
#     print(i[0], '-', t_celsius, 'C')

stream = [
    '2018-01-01,user1,3',
    '2018-01-07,user1,4',
    '2018-03-29,user1,1',
    '2018-04-04,user1,13',
    '2018-01-05,user2,7',
    '2018-06-14,user3,4',
    '2018-07-02,user3,10',
    '2018-03-21,user4,19',
    '2018-03-22,user4,4',
    '2018-04-22,user4,8',
    '2018-05-03,user4,9',
    '2018-05-11,user4,11',
]

sum = 0
user_zero = ''
cnt = 0
for i in stream:
    num = int((i.split(','))[2])
    sum += num
    user_unic = i.split(',')[1]
    if user_unic != user_zero:
        cnt += 1
        user_zero = user_unic

print('Среднее количество просмотров на уникального пользователя: ', round(sum/cnt, 2))


# st = input()
# first_list = sorted(list(''.join(st.split())))
# finish_list = []
# for i in first_list:
#     cnt = first_list.count(i)
#     if  i not in finish_list:
#         if cnt > 1:
#             finish_list.append(i)
#
# print(" ".join(map(str, finish_list)))
# print(*finish_list)
