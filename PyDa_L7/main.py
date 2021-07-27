
import requests
from libs.exchange import Rate



class Rate:
    def __init__(self, format_='value', diff=True): #по мере разумения задания, добавил
        # дополнительный параметр, правда не соображу, когда менять на False
        self.format = format_
        self.diff = diff

    def exchange_rates(self):
        """
        Возвращает ответ сервиса с информацией о валютах в виде:

        {
            'AMD': {
                'CharCode': 'AMD',
                'ID': 'R01060',
                'Name': 'Армянских драмов',
                'Nominal': 100,
                'NumCode': '051',
                'Previous': 14.103,
                'Value': 14.0879
                },
            ...
        }
        """
        self.r = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        return self.r.json()['Valute']

    def make_format(self, currency):
        """
        Возвращает информацию о валюте currency в двух вариантах:
        - полная информация о валюте при self.format = 'full':
        Rate('full').make_format('EUR')
        {
            'CharCode': 'EUR',
            'ID': 'R01239',
            'Name': 'Евро',
            'Nominal': 1,
            'NumCode': '978',
            'Previous': 79.6765,
            'Value': 79.4966
        }

        Rate('value').make_format('EUR')
        79.4966
        """
        response = self.exchange_rates()

        if currency in response:
            if self.format == 'full':
                return response[currency]

            if self.format == 'value' and self.diff:#проверяю параметр diff на истину
                result = response[currency]['Previous'] - response[currency]['Value']
                return result

        return 'Error'

    def eur(self):
        """Возвращает курс евро на сегодня в формате self.format"""
        return self.make_format('EUR')

    def usd(self):
        """Возвращает курс доллара на сегодня в формате self.format"""
        return self.make_format('USD')

    def brl(self):
        """Возвращает курс бразильского реала на сегодня в формате self.format"""
        return self.make_format('BRL')

    def max_rate_diff(self):
        '''
        Задание 1
        Напишите функцию, которая возвращает название валюты
        (поле ‘Name’) с максимальным значением курса с помощью
        сервиса www.cbr-xml-daily.ru...ly_json.js
        '''
        response = self.exchange_rates()
        print('Максимальное значение валюты:')
        for key in response.keys():
            if response[key]['Value'] >= response[key]['Previous']:
                print(key, 'Сегодня выше, чем вчера:', response[key]['Value'])
            else:
                print(key, 'Вчера было выше, чем сегодня:', response[key]['Previous'])



r = Rate(format_='value')
print(r.usd())
r.max_rate_diff()

