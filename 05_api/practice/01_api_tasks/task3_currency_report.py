# module_05_api/practice/01_api_tasks/task3_currency_report.py
"""
Задание 3. Отчёт и конвертация валют

Продолжаем работать с курсами валют. Пусть rates — это словарь вида
{CharCode: курс_float}, который вы получаете функцией get_all_rates из
задания 2.

    rates = {
        'USD': 77.2736,
        'EUR': 91.2965,
        'JPY': 0.496107,
        'GBP': 104.4353,
    }

Напишите функции для анализа и конвертации.
"""


def highest_rate(rates):
    """
    Возвращает код валюты с самым высоким курсом (наибольший VunitRate).

    Параметры:
        rates (dict): словарь {код валюты: курс}.

    Возвращает:
        str: код валюты с максимальным курсом.
    """
    # НАПИШИТЕ ВАШ КОД ЗДЕСЬ
    return max(rates, key=rates.get)


def lowest_rate(rates):
    """
    Возвращает код валюты с самым низким курсом (наименьший VunitRate).

    Параметры:
        rates (dict): словарь {код валюты: курс}.

    Возвращает:
        str: код валюты с минимальным курсом.
    """
    # НАПИШИТЕ ВАШ КОД ЗДЕСЬ
    return min(rates, key=rates.get)


def convert(rates, amount, from_code, to_code):
    """
    Конвертирует сумму amount из валюты from_code в валюту to_code.

    Все курсы заданы в рублях (сколько рублей стоит одна единица валюты).

    Алгоритм:
        1. Перевести amount из from_code в рубли:
           rub = amount * rates[from_code]
        2. Перевести рубли в to_code:
           result = rub / rates[to_code]

    Параметры:
        rates (dict): словарь {код валюты: курс}.
        amount (float): сумма в исходной валюте.
        from_code (str): код исходной валюты.
        to_code (str): код целевой валюты.

    Возвращает:
        float: сумма в целевой валюте.
    """
    # НАПИШИТЕ ВАШ КОД ЗДЕСЬ
    rub = amount * rates[from_code]
    return rub / rates[to_code]


def top_expensive(rates, n):
    """
    Возвращает список из n кодов валют с самыми высокими курсами,
    отсортированный по убыванию курса.

    Параметры:
        rates (dict): словарь {код валюты: курс}.
        n (int): количество валют в топе.

    Возвращает:
        list: список кодов валют (d[0] — самая дорогая валюта).
    """
    # НАПИШИТЕ ВАШ КОД ЗДЕСЬ
    return sorted(rates, key=rates.get, reverse=True)[:n]
