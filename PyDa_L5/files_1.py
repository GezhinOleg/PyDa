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
                purchases[key] = purchases[key] + ',' + dict_['category']
            else:
                purchases[key] = (dict_['category'])
    with open("purchases_dict.txt", "w", encoding="utf-8") as file:
        json.dump(purchases, file, indent=2, ensure_ascii=False)


def main():
    read_purchase('purchase_log.txt')


if __name__ == '__main__':
    main()
# Если значения 'user_id' в исходном файле совпадают, то к значению по
# данному ключу прибавляется строка покупок.
