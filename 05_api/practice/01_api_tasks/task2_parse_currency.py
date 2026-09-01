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
    """
    Возвращает курс указанной валюты в виде float.

    Параметры:
        data (dict): словарь с данными ЦБ РФ (структура выше).
        code (str): код валюты, например 'USD', 'EUR', 'JPY'.

    Возвращает:
        float: курс заданной валюты (VunitRate, приведённый к float),
               или None, если валюта с таким кодом не найдена.

    Подсказка: переберите данные data['ValCurs']['Valute'] и сравните
    valute['CharCode'] с code. Для получения float используйте VunitRate.
    """
    # НАПИШИТЕ ВАШ КОД ЗДЕСЬ
    valutes = data['ValCurs']['Valute']
    for valute in valutes:
        if valute['CharCode'] == code:
            return float(valute['VunitRate'].replace(',', '.'))
    return None


def get_all_rates(data):
    """
    Возвращает словарь {CharCode: курс_float} для всех валют из data.

    Параметры:
        data (dict): словарь с данными ЦБ РФ.

    Возвращает:
        dict: словарь, где ключ — код валюты, значение — её курс (float).
    """
    # НАПИШИТЕ ВАШ КОД ЗДЕСЬ
    rates = {}
    valutes = data['ValCurs']['Valute']
    for valute in valutes:
        rates[valute['CharCode']] = float(valute['VunitRate'].replace(',', '.'))
    return rates
