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
"""


def best_currency_to_travel(rates, budget):
    """
    Возвращает код валюты, в которой за budget рублей можно получить
    больше всего единиц иностранной валюты.

    Параметры:
        rates (dict): словарь {код валюты: курс}.
        budget (float): бюджет в рублях.

    Возвращает:
        str: код валюты с минимальным курсом (наиболее выгодной для обмена).
    """
    # НАПИШИТЕ ВАШ КОД ЗДЕСЬ
    return min(rates, key=rates.get)


def how_much_you_get(rates, budget, code):
    """
    Возвращает, сколько единиц валюты code можно получить за budget рублей.

    Параметры:
        rates (dict): словарь {код валюты: курс}.
        budget (float): бюджет в рублях.
        code (str): код целевой валюты.

    Возвращает:
        float: количество единиц валюты code (budget / rates[code]).
    """
    # НАПИШИТЕ ВАШ КОД ЗДЕСЬ
    return budget / rates[code]


def currency_trend(rate_today, rate_yesterday, code):
    """
    Сравнивает курс валюты code сегодня и вчера.

    Параметры:
        rate_today (dict): словарь {код валюты: курс} на сегодня.
        rate_yesterday (dict): словарь {код валюты: курс} на вчера.
        code (str): код валюты.

    Возвращает:
        dict: словарь вида
              {'code': code,
               'today': курс_сегодня,
               'yesterday': курс_вчера,
               'change': разница (today - yesterday),
               'direction': 'up' если курс вырос, 'down' если упал,
                            'same' если не изменился}
    """
    # НАПИШИТЕ ВАШ КОД ЗДЕСЬ
    today = rate_today[code]
    yesterday = rate_yesterday[code]
    change = today - yesterday
    if change > 0:
        direction = 'up'
    elif change < 0:
        direction = 'down'
    else:
        direction = 'same'
    return {
        'code': code,
        'today': today,
        'yesterday': yesterday,
        'change': change,
        'direction': direction,
    }


def format_rate_table(rates):
    """
    Форматирует курсы валют в виде красивой таблицы (строчную строку).

    Каждая строка имеет вид:
        "{код}: {курс:.2f} руб."

    Строки разделяются символом новой строки "\\n". Порядок строк —
    по возрастанию курса (от самой дешёвой валюты к самой дорогой).

    Параметры:
        rates (dict): словарь {код валюты: курс}.

    Возвращает:
        str: многострочная строка с отформатированной таблицей.
    """
    # НАПИШИТЕ ВАШ КОД ЗДЕСЬ
    lines = []
    for code in sorted(rates, key=rates.get):
        lines.append(f"{code}: {rates[code]:.2f} руб.")
    return "\n".join(lines)
