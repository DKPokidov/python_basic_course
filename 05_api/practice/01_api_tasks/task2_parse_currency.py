# module_05_api/practice/01_api_tasks/task2_parse_currency.py
"""
Задание 2. Парсинг курсов валют

Вы уже умеете получать данные от API ЦБ РФ и преобразовывать их в словарь.
Теперь напишите функции для извлечения курсов отдельных валют из этого словаря.

Предположим, data — это словарь, полученный из xmltodict.parse, например:

    data = {
        'ValCurs': {
            '@Date': '28.02.2026',
            'Valute': [
                {
                    'CharCode': 'USD',
                    'Nominal': '1',
                    'Name': 'Доллар США',
                    'Value': '77,2736',
                    'VunitRate': '77,2736',
                },
                {
                    'CharCode': 'EUR',
                    'Nominal': '1',
                    'Name': 'Евро',
                    'Value': '91,2965',
                    'VunitRate': '91,2965',
                },
                {
                    'CharCode': 'JPY',
                    'Nominal': '100',
                    'Name': 'Иен',
                    'Value': '49,6107',
                    'VunitRate': '0,496107',
                },
            ]
        }
    }

Обратите внимание: значения курсов хранятся как строки с запятой в качестве
разделителя (например, '77,2736'). Вам нужно преобразовывать их в float,
заменяя запятую на точку: float('77,2736'.replace(',', '.')) -> 77.2736.
"""


def get_currency_rate(data, code):
    pass


def get_all_rates(data):
    pass