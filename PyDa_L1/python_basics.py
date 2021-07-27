# '''
# Фразы для теста.
# Насколько проще было бы писать программы, если бы не заказчики
# 640Кб должно хватить для любых задач. Билл Гейтс (по легенде)
# '''
#
# phrase_1 = input()
# phrase_2 = input()
#
# if phrase_1 > phrase_2:
#   print('Фраза 1 длиннее фразы 2')
# elif phrase_2 > phrase_1:
#   print('Фраза 2 длиннее фразы 1')
# else:
#   print('Фразы равной длины')

# year = int(input())
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print('Високосный год')
# else:
#     print('Обычный год')

#zodiac
# month_born = input('Введите название месяца: ')
# data_born = int(input('Введите дату рождения: '))
# if month_born == 'январь' and data_born <= 22 or month_born == 'декабрь' and data_born <= 31 and data_born >= 23:
#   print ('козерог')
#
# elif month_born == 'февраль' and data_born <= 22 or month_born == 'январь' and data_born <= 31 and data_born >= 23:
#   print ('водолей')
#
# elif month_born == 'март' and data_born <= 22 or month_born == 'февраль' and data_born <= 28 and data_born >= 23:
#   print ('рыбы')
#
# elif month_born == 'апрель' and data_born <= 22 or month_born == 'март' and data_born <= 31 and data_born >= 23:
#   print ('овен')
#
# elif month_born == 'май' and data_born <= 22 or month_born == 'апрель' and data_born <= 30 and data_born >= 23:
#   print ('телец')
#
# elif month_born == 'июнь' and data_born <= 22 or month_born == 'май' and data_born <= 31 and data_born >= 23:
#   print ('близнецы')
#
# elif month_born == 'июль' and data_born <= 22 or month_born == 'июнь' and data_born <= 30 and data_born >= 23:
#   print ('рак')
#
# elif month_born == 'август' and data_born <= 22 or month_born == 'июль' and data_born <= 31 and data_born >= 23:
#   print ('лев')
#
# elif month_born == 'сентябрь' and data_born <= 22 or month_born == 'август' and data_born <= 31 and data_born >= 23:
#   print ('дева')
#
# elif month_born == 'октябрь' and data_born <= 22 or month_born == 'сентябрь' and data_born <= 30 and data_born >= 23:
#   print ('весы')
#
# elif month_born == 'ноябрь' and data_born <= 22 or month_born == 'октябрь' and data_born <= 31 and data_born >= 23:
#   print ('скорпион')
#
# elif month_born == 'декабрь' and data_born <= 22 or month_born == 'ноябрь' and data_born <= 30 and data_born >= 23:
#   print ('стрелец')
#
# else:
#   print('Вы что-то неправильно ввели, попробуйте ещё раз!')


# width = int(input('Введите значение ширины:'))
# length = int(input('Введите значение длины:'))
# height = int(input('Введите значение высоты:'))
#
# if width < 15 and length < 15 and height < 15:
#   print('Коробка №1')
# elif 15 <= width < 50 and 15 <= length < 50 and 15 <= height < 50:
#   print('Коробка №2')
# elif length > 200:
#   print('Упаковка для лыж')
# else:
#   print('Стандартная коробка №3')

# number_tiket = int(input())
# num1 = number_tiket//100000+number_tiket//10000%10+number_tiket//1000%10
# num2 = number_tiket//100%10+number_tiket//10%10+number_tiket%10
# if num1 == num2:
#     print('Счастливый билет')
# else:
#     print('Несчастливый билет')
# 
# figure = input('Введите название фигуры, варианты - круг, прямоугольник, треугольник:')
#
# if figure == 'круг':
#     r = int(input('Введите радиус круга:'))
#     print('Площадь круга:', r**2*3.14)
# elif figure == 'треугольник':
#     a = float(input('Введите длину стороны A:'))
#     b = float(input('Введите длину стороны B:'))
#     c = float(input('Введите длину стороны C:'))
#     p = (a+b+c)/2
#     s = (p*(p-a)*(p-b)*(p-c))**0.5
#     print('Площадь треугольника:', s)
# elif figure == 'прямоугольник':
#     a = int(input('Введите длину стороны A:'))
#     b = int(input('Введите длину стороны B:'))
#     print('Площадь прямоугольника:',a*b)
#
# else:
#     print('Вы ввели неверное название фигуры, попробуйте ещё раз!')
