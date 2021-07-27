'''
1    Переведите содержимое файла purchase_log.txt в словарь purchases вида:
    {‘1840e0b9d4’: ‘Продукты’, …}

2    Для каждого user_id в файле visit_log.csv определите третий столбец с
    категорией покупки (если покупка была, сам файл visit_log.csv изменять
    не надо). Запишите в файл funnel.csv визиты из файла visit_log.csv, в
    которых были покупки с указанием категории.
    Учтите условия на данные:
    содержимое purchase_log.txt помещается в оперативную память компьютера
    содержимое visit_log.csv - нет; используйте только построчную обработку
    этого файла
'''
from pprint import pprint
import json


def read_purchase(file_path):
    purchases = {}
    key = ''
    vel = []
    i = 0
    with open(file_path, encoding = 'utf-8') as f:
        f.readline()
        for line in f:
            line = line.strip()
            dict_ = json.loads(line)
            key = dict_['user_id']
            if key in purchases:
                purchases[key] = purchases[key] + '|' + dict_['category']
            else:
                purchases[key] = (dict_['category'])
    return purchases

def read_csv(file_path, purch):
    with open(file_path, encoding='utf-8') as f:
        with open('funnel.csv', 'w', encoding='utf-8') as f2write:
            line = f.readline().strip() + ',' + 'category \n'
            f2write.write(line)
            i = 0
            for line in f:
                j = line.strip().split(',')[0]
                if j in purch:
                    st = line.strip()+ ',' + purch[j] + '\n'
                    f2write.write(st)

def main():
    p_dict = read_purchase('purchase_log.txt')
    read_csv('visit_log.csv', p_dict)

if __name__ == '__main__':
    main()






#
# # with open("purchases_dict.json", "w", encoding="utf-8") as file:
# #     json.dump(purchases, file, indent=2, ensure_ascii=False)
#
# def read_csv(file_path, purch):
#     with open(file_path, encoding='utf-8') as f:
#         # with open('funnel.csv', 'w', encoding='utf-8') as f2write:
#             line = f.readline().strip() + ',' + 'category \n'
#             f2write.write(line)
#             print(line)
#             i = 0
#             j = ''
#             lst = []
#             for line in f:
#                 j = line.strip().split(',')[0]
#                 # if k == j:
#                 #     line = line.strip() + ',' + purch[k] + '\n'
#                     # f2write.write(line)
#
#
#
#
#
# def main():
#     p_dict = read_purchase('purchase_log.txt')
#     read_csv('visit_log.csv', p_dict)
#
# if __name__ == '__main__':
#     main()
