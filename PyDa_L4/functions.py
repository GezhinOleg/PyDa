documents = [
 {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
 {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
 {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]

directories = {
 '1': ['2207 876234', '11-2'],
 '2': ['10006'],
 '3': []
}
'''
p - Пользователь может узнать владельца документа по его номеру
s - Пользователь может по номеру документа узнать на какой полке он хранится
l - Пользователь может увидеть полную информацию по всем документам
ads - Пользователь может добавить новую полку
ds - Пользователь может удалить существующую полку из данных (только если она пустая)
ad - Пользователь может добавить новый документ в данные
'''

def person_document(doc_list):
    result = 'Извините, введенный номер в базе отсутствует!'
    doc_input = input('Введите номер документа:')
    for i in doc_list:
        if doc_input == i['number']:
            result = i['name']
    return result

def shelf_document(shelf):
    number_doc = input('Введите номер документа: ')
    result = 'Извините, введенный номер в базе отсутствует!'
    for shelf_l, doc in shelf.items():
        for j in doc:
            if number_doc == j:
                result =  f'Лежит на полке № {shelf_l}'
    return result

def list_all_document(doc_list, shelf):
    summary_dictionary = {}
    for doc in doc_list:
        for i in shelf:
            for j in shelf[i]:
                if j == doc['number']:
                     print('№: ', doc['number'], ', тип: ', doc['type'], ', владелец: ', doc['name'], ', полка хранения: ', i, sep = '')

def add_shelf(shelf):
    new_shelf = input('Введите номер полки ')
    if new_shelf not in directories:
      directories[new_shelf] = []
      print('Полка добавлена. Текущий перечень полок:', ",  ".join(map(str, directories)))
    elif new_shelf in directories:
      print('Такая полка уже существует. Текущий перечень полок:', ",  ".join(map(str, directories)))

def delete_shelf(shelf):
    del_shelf = input('Введите номер полки ')
    if del_shelf in shelf:
        if shelf[del_shelf] == []:
            del shelf[del_shelf]
            print('Полка удалена. Текущий перечень полок:', ",  ".join(map(str, shelf.keys())))
        elif shelf[del_shelf] != []:
            print('На полке есть документа, удалите их перед удалением полки. Текущий перечень полок:', ",  ".join(map(str, shelf.keys())))
    else:
        print('Такой полки не существует. Текущий перечень полок:', ",  ".join(map(str, shelf.keys())))

def add_document(doc_list, shelf):
    doc_new = {}
    doc_new['number'] = input('Введите номер документа: ')
    doc_new['type'] = input('Введите тип документа: ')
    doc_new['name'] = input('Введите владельца документа: ')
    num_shelf = input('Введите полку для хранения: ')
    if num_shelf in shelf.keys():
        shelf[num_shelf].append(doc_new['number'])
        doc_list.append(doc_new)
        print('Документ добавлен. Текущий список документов:', List_All_Document(documents, directories))
        # Почему-то выводит список, с добавленным файлом и в конце прописывает
        #[None]
    else:
        print('Такой полки не существует. Добавьте полку командой ads.')
        print(list_all_document(documents, directories))
# Сделал только функцию добавления документа, Остальные пункты, понимаю как делать,
# но не могу себя заставить, примечание (необязательное) сильно расхолаживает.

def main():
    while True:
        print('Для работы с программой введите команды: p, s, l, ads, ds, ad')
        user_input = input('Введите команду: ')
        if user_input == 'p':
            print(person_document(documents))
        elif user_input == 's':
            print(shelf_document(directories))
        elif user_input == 'l':
            list_all_document(documents, directories)
        elif user_input == 'ads':
            add_shelf(directories)
        elif user_input == 'ds':
            delete_shelf(directories)
        elif user_input == 'ad':
            add_document(documents, directories)
        elif user_input == 'q':
            print('До свидания!')
            break
main()

# Попытался сделать вызов функций через словарь, первые две получилось нормально,
# потом из-за ввода параметров к функции началась путаница, решил не ломать, то что работает.
# def main():
#     while True:
#         print('Для работы с программой введите команды: p, s, l, ads, ds, ad, d, m')
#         user_input = input('Введите команду: ')
#         command_user = {'p': 'Person_Document(documents)', 's': 'Shelf_Document(directories)', 'l': 'List_All_Document(documents, directories)',
#         'ads': add_shelf}
#         if user_input == 'q':
#              print('До свидания!')
#              break
#         elif user_input in command_user:
#             command_user[user_input]()
#         else:
#             print('Введите правильную команду.')
#
# main()

# Попытался сделать вызов функций через словарь, первые две получилось нормально,
# потом из-за ввода параметров к функции началась путаница, решил не ломать, то что работает.
# def main():
#     while True:
#         print('Для работы с программой введите команды: p, s, l, ads, ds, ad, d, m')
#         user_input = input('Введите команду: ')
#         command_user = {'p': 'Person_Document(documents)', 's': 'Shelf_Document(directories)', 'l': 'List_All_Document(documents, directories)',
#         'ads': add_shelf}
#         if user_input == 'q':
#              print('До свидания!')
#              break
#         elif user_input in command_user:
#             command_user[user_input]()
#         else:
#             print('Введите правильную команду.')
#
# main()
