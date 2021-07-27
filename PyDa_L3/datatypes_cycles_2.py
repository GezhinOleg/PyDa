# '''
# Дана переменная, в которой хранится словарь, содержащий гео-метки
# для каждого пользователя (пример структуры данных приведен ниже).
# Вам необходимо написать программу, которая выведет на экран
# множество уникальных гео-меток всех пользователей.
# Пример работы программы:
#
# Результат: {98, 35, 15, 213, 54, 119}
# '''
# ids = {'user1': [213, 213, 213, 15, 213],
#        'user2': [54, 54, 119, 119, 119],
#        'user3': [213, 98, 98, 35]}
#
# ids_set = {}
# ids_lst = []
# for i in ids.values():
#     for j in i:
#         ids_lst.append(j)
# ids_set = set(ids_lst)
# print(ids_set)

# '''
# Дана переменная, в которой хранится список поисковых запросов пользователя
# (пример структуры данных приведен ниже). Вам необходимо написать программу,
# которая выведет на экран распределение количества слов в запросах в требуемом виде.
# Пример работы программы:
# queries = [
#     'смотреть сериалы онлайн',
#     'новости спорта',
#     'афиша кино',
#     'курс доллара',
#     'сериалы этим летом',
#     'курс по питону',
#     'сериалы про спорт',
# ]
# Результат:
# Поисковых запросов, содержащих 2 слов(а): 42.86%
# Поисковых запросов, содержащих 3 слов(а): 57.14%
# '''
# queries = [
#     'смотреть сериалы онлайн',
#     'новости спорта',
#     'афиша кино',
#     'курс доллара',
#     'сериалы этим летом',
#     'курс по питону',
#     'сериалы про спорт',
# ]
# count_list = []
# for i in queries:
#     count_list.append(len(i.split(' ')))
#
# dct = {}
# for j in count_list:
#     if j in dct:
#         dct[j] += 1
#     else:
#         dct[j] = 1
# for item in sorted(dct):
#     print('Поисковых запросов, содержащих', item, 'слов(а):', round((dct[item]*100/len(count_list)), 2), '%')

# '''
# Дана переменная, в которой хранится информация о затратах и доходе рекламных
# кампаний по различным источникам. Необходимо дополнить исходную
# структуру показателем ROI, который рассчитаем по формуле:
# (revenue / cost - 1) * 100
# Пример работы программы:
# results = {
#     'vk': {'revenue': 103, 'cost': 98},
#     'yandex': {'revenue': 179, 'cost': 153},
#     'facebook': {'revenue': 103, 'cost': 110},
#     'adwords': {'revenue': 35, 'cost': 34},
#     'twitter': {'revenue': 11, 'cost': 24},
# }
# Результат:
# {'adwords': {'revenue': 35, 'cost': 34, 'ROI': 2.94},
#  'facebook': {'revenue': 103, 'cost': 110, 'ROI': -6.36},
#  'twitter': {'revenue': 11, 'cost': 24, 'ROI': -54.17},
#  'vk': {'revenue': 103, 'cost': 98, 'ROI': 5.1},
#  'yandex': {'revenue': 179, 'cost': 153, 'ROI': 16.99}}
#  '''
# from pprint import pprint
# results = {
#     'vk': {'revenue': 103, 'cost': 98},
#     'yandex': {'revenue': 179, 'cost': 153},
#     'facebook': {'revenue': 103, 'cost': 110},
#     'adwords': {'revenue': 35, 'cost': 34},
#     'twitter': {'revenue': 11, 'cost': 24},
# }
#
# for i in results.values():
#     i['ROI'] = round(((i['revenue'] / i['cost'] - 1) * 100), 2)
# pprint(results)

# '''
# Дана переменная, в которой хранится статистика рекламных каналов по объемам
# продаж (пример структуры данных приведен ниже). Напишите программу,
# которая возвращает название канала с максимальным объемом продаж.
# Пример работы программы:
# stats = {'facebook': 55, 'yandex': 115, 'vk': 120, 'google': 99, 'email': 42, 'ok': 98}
# Результат: Максимальный объем продаж на рекламном канале: vk
# '''
#
# stats = {'facebook': 55, 'yandex': 115, 'vk': 120, 'google': 99, 'email': 42, 'ok': 98}
# max = stats['facebook']
# max_key = ''
# for k, v in stats.items():
#     if v > max:
#         max = v
#         max_key = k
#
# print('Максимальный объем продаж на рекламном канале:', max_key)

# '''
# Дан список произвольной длины. Необходимо написать код, который на основе
# исходного списка составит словарь такого уровня вложенности, какова длина
# исхондого списка.
# Примеры работы программы:
#     my_list = ['2018-01-01', 'yandex', 'cpc', 100]
# Результат: {'2018-01-01': {'yandex': {'cpc': 100}}}
#     my_list = ['a', 'b', 'c', 'd', 'e', 'f']
# Результат: {'a': {'b': {'c': {'d': {'e': 'f'}}}}}
# '''
#
# my_list = ['a', 'b', 'c', 'd', 'e', 'f']
#
# finish_dict = {my_list[-2]: my_list[-1]}
# for i in my_list[:-2][::-1]:
#     finish_dict = {i: finish_dict}
# print(finish_dict)

'''
Дана книга рецептов с информацией о том, сколько ингредиентов нужно для
приготовления блюда в расчете на одну порцию (пример данных представлен ниже).
Напишите программу, которая будет запрашивать у пользователя количество
порций для приготовления этих блюд и отображать информацию о суммарном
количестве требуемых ингредиентов в указанном виде.
Внимание! Одинаковые ингридиенты с разными размерностями нужно считать
раздельно! Пример работы программы:

cook_book = {
  'салат': [
     {'ingridient_name': 'сыр', 'quantity': 50, 'measure': 'гр'},
     {'ingridient_name': 'томаты', 'quantity': 2, 'measure': 'шт'},
     {'ingridient_name': 'огурцы', 'quantity': 20, 'measure': 'гр'},
     {'ingridient_name': 'маслины', 'quantity': 10, 'measure': 'гр'},
     {'ingridient_name': 'оливковое масло', 'quantity': 20, 'measure': 'мл'},
     {'ingridient_name': 'салат', 'quantity': 10, 'measure': 'гр'},
     {'ingridient_name': 'перец', 'quantity': 20, 'measure': 'гр'}
    ],
  'пицца': [
     {'ingridient_name': 'сыр', 'quantity': 20, 'measure': 'гр'},
     {'ingridient_name': 'колбаса', 'quantity': 30, 'measure': 'гр'},
     {'ingridient_name': 'бекон', 'quantity': 30, 'measure': 'гр'},
     {'ingridient_name': 'оливки', 'quantity': 10, 'measure': 'гр'},
     {'ingridient_name': 'томаты', 'quantity': 20, 'measure': 'гр'},
     {'ingridient_name': 'тесто', 'quantity': 100, 'measure': 'гр'},
    ],
  'лимонад': [
     {'ingridient_name': 'лимон', 'quantity': 1, 'measure': 'шт'},
     {'ingridient_name': 'вода', 'quantity': 200, 'measure': 'мл'},
     {'ingridient_name': 'сахар', 'quantity': 10, 'measure': 'гр'},
     {'ingridient_name': 'лайм', 'quantity': 20, 'measure': 'гр'},
    ]
}
Введите количество порций:
3
Результат:
Сыр: 210 гр
Томаты: 6 шт
Огурцы: 60 гр
Маслины: 30 гр
Оливковое масло: 60 мл
Салат: 30 гр
Перец: 60 гр
Колбаса: 90 гр
Бекон: 90 гр
Оливки: 30 гр
Томаты: 60 гр
Тесто: 300 гр
Лимон: 3 шт
Вода: 600 мл
Сахар: 30 гр
Лайм: 60 гр
'''

cook_book = {
  'салат': [
     {'ingridient_name': 'сыр', 'quantity': 50, 'measure': 'гр'},
     {'ingridient_name': 'томаты', 'quantity': 2, 'measure': 'шт'},
     {'ingridient_name': 'огурцы', 'quantity': 20, 'measure': 'гр'},
     {'ingridient_name': 'маслины', 'quantity': 10, 'measure': 'гр'},
     {'ingridient_name': 'оливковое масло', 'quantity': 20, 'measure': 'мл'},
     {'ingridient_name': 'салат', 'quantity': 10, 'measure': 'гр'},
     {'ingridient_name': 'перец', 'quantity': 20, 'measure': 'гр'}
    ],
  'пицца': [
     {'ingridient_name': 'сыр', 'quantity': 20, 'measure': 'гр'},
     {'ingridient_name': 'колбаса', 'quantity': 30, 'measure': 'гр'},
     {'ingridient_name': 'бекон', 'quantity': 30, 'measure': 'гр'},
     {'ingridient_name': 'оливки', 'quantity': 10, 'measure': 'гр'},
     {'ingridient_name': 'томаты', 'quantity': 20, 'measure': 'гр'},
     {'ingridient_name': 'тесто', 'quantity': 100, 'measure': 'гр'},
    ],
  'лимонад': [
     {'ingridient_name': 'лимон', 'quantity': 1, 'measure': 'шт'},
     {'ingridient_name': 'вода', 'quantity': 200, 'measure': 'мл'},
     {'ingridient_name': 'сахар', 'quantity': 10, 'measure': 'гр'},
     {'ingridient_name': 'лайм', 'quantity': 20, 'measure': 'гр'},
    ]
}
from pprint import pprint

n = int(input('Введите количество порций: '))
key = ''
value = []
final_dict = {}
for i in cook_book.values():
    for j in i:
        key = j['ingridient_name']
        if key not in final_dict:
            final_dict[key] = [j['quantity'], j['measure']]
        elif key in final_dict:
            final_dict[key][0] += j['quantity']

for _ in final_dict:
    final_dict[_][0] *= n

for key, value in final_dict.items():
  print(key, ":", " ".join(map(str, value)))

# pprint(final_dict)
