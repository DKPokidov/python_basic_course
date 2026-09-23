# module_05_api/practice/01_api_tasks/task4_savings.py
"""
Задание 4. Прикладная задача: планирование путешествия

Вы собираетесь в путешествие и используете курсы ЦБ РФ, чтобы решить,
в какой валюте выгоднее везти бюджет. Все курсы заданы в рублях за единицу
иностранной валюты (VunitRate).

Пример данных rates (словарь {код валюты: курс}):
    rates = {
        'USD': 77.2736,
        'EUR': 91.2965,
        'JPY': 0.496107,
        'GBP': 104.4353,
        'CNY': 11.2394,
    }

Чем ниже курс валюты, тем больше иностранной валюты можно получить
за фиксированную сумму рублей.

Напишите четыре функции:

best_currency_to_travel(rates, budget) -> str
    Возвращает код валюты, в которой за бюджет рублей получится больше всего
    денег (то есть код валюты с наименьшим курсом).

how_much_you_get(rates, budget, code) -> float
    Возвращает, сколько единиц валюты code можно получить за budget рублей:
        budget / rates[code]

currency_trend(rates_today, rates_yesterday, code) -> dict
    Сравнивает курс валюты сегодня и вчера. Возвращает словарь:
        {
            'code': код_валюты,
            'today': курс_сегодня,
            'yesterday': курс_вчера,
            'change': курс_сегодня - курс_вчера,
            'direction': 'up' | 'down' | 'same',
        }
    direction равен 'up', если курс вырос (change > 0), 'down' — если упал
    (change < 0), и 'same' — если не изменился (change == 0.0).

format_rate_table(rates) -> str
    Возвращает многострочную строку с курсами, отсортированными по возрастанию
    курса (самая дешёвая валюта — первая строка). Каждая строка имеет вид:
        'JPY: 0.50 руб.'
    Курс округляется до двух знаков после запятой (f'{курс:.2f}').
    Строки разделяются символом перевода строки '\\n'.
"""


def best_currency_to_travel(rates, budget):
    pass


def how_much_you_get(rates, budget, code):
    pass


def currency_trend(rates_today, rates_yesterday, code):
    pass


def format_rate_table(rates):
    pass