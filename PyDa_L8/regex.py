'''
Задание 1
Напишите функцию, которая принимает на вход строку и проверяет является ли она
валидным транспортным номером (1 буква, 3 цифры, 2 буквы, 2-3 цифры).
Обратите внимание, что не все буквы кириллического алфавита используются в
транспортных номерах.
Если номер валиден, то функция должна возвращать отдельно номер и регион.
Примеры работы программы:
    car_id = 'A222BC96'
Результат: Номер A222BС валиден. Регион: 96
    car_id = 'АБ22ВВ193'
Результат: Номер не валиден
'''

import re


def valid_number(str_car_number):
    result = ''
    try:
        car_number = re.compile(r'(^[АВЕКМНОРСТУХABEKMHOPCTYX]\d{3}(?<!000)[АВЕКМНОРСТУХABEKMHOPCTYX]{2})(\d{2,3}$)')
        valid_number = car_number.search(str_car_number)
        result = f'Номер {valid_number.group(1)} валиден. Регион: {valid_number.group(2)}'
    except Exception:
        result = 'Номер не валиден.'
    return result
'''
Напишите функцию, которая будет удалять все последовательные повторы
слов из заданной строки при помощи регулярных выражений.
'''
def string_split(str_sp):
    string_be_split = re.sub(r'\b([^\W\d_]+)(\s+\1)+\b', r'\1', str_sp)
    return string_be_split
'''
Напишите функцию, которая будет возвращать акроним по переданной в
нее строке со словами.
'''
def string_upper(str_sp):
    string_be_split =  re.findall(r'\b\w', str_sp)
    # st = string_be_split.search(str_sp)
    result = (''.join(string_be_split)).upper()
    return result
'''
Напишите функцию, которая будет принимать на вход список email-адресов и
выводить их распределение по доменным зонам.
'''
def email_domian():
    emails = ['test@gmail.com', 'xyz@test.in', 'test@ya.ru', 'xyz@mail.ru', 'xyz@ya.ru', 'xyz@gmail.com']
    email_string = ','.join(emails)
    e_lst = re.findall(r'@\w+.\w+', email_string)
    cnt_lst = []
    for i in e_lst:
        if i in cnt_lst:
            continue
        else:
            cnt_lst.append(i)
            print(i, ':', e_lst.count(i))
'''
Напишите функцию, которая будет подсчитывать сколько слов начинается на
гласные, а сколько на согласные буквы в тексте (текст может быть написан
как с использованием букв кириллицы, так и латиницы).
'''
def get_vowels_consonants(some_text):
    count_vowels = re.findall(r'\b[aeiouAEIOUаеёиоуыэюяАЕЁИОУЫЭЮЯ]\w+', some_text)
    count_consonants = re.findall(r'\b[^aeiouAEIOUаеёиоуыэюяАЕЁИОУЫЭЮЯ ]\w+', some_text)
    print('Слов на гласные буквы: ', len(count_vowels))
    print('Слов на согласные буквы: ', len(count_consonants))


if __name__ == '__main__':
    call = input('Введите n, st, ak, em, cn и нажмите Enter: ')
    if call == 'n':
        print(valid_number('А222BC96'))
    elif call == 'st':
        print(string_split(r'Напишите функцию функцию, которая будет будет будет будет удалять все все все все последовательные повторы слов из из из из заданной строки строки при помощи регулярных выражений.'))
    elif call == 'ak':
        print(string_upper('Напишите функцию'))
    elif call == 'em':
        email_domian()
    elif call == 'cn':
        get_vowels_consonants(r'Эталонной реализацией Python является интерпретатор CPython, поддерживающий большинство активно используемых платформ. Он распространяется под свободной лицензией Python Software Foundation License, позволяющей использовать его без ограничений в любых приложениях, включая проприетарные.')
    elif call == 'cn':
        get_vowels_consonants()
