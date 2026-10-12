# module_05_api/practice/01_api_tasks/task1_fetch_rates.py
"""
Задание 1. Получение курсов валют с сайта ЦБ РФ

Напишите функции для выполнения HTTP-запроса к API Центрального банка РФ
и обработки ответа.

API ЦБ РФ возвращает курсы валют на текущий день в формате XML:
    https://www.cbr.ru/scripts/XML_daily.asp

Пример ответа (упрощённо):
    <ValCurs Date="28.02.2026" name="Foreign Currency Market">
      <Valute ID="R01235">
        <NumCode>840</NumCode>
        <CharCode>USD</CharCode>
        <Nominal>1</Nominal>
        <Name>Доллар США</Name>
        <Value>77,2736</Value>
      </Valute>
      ...
    </ValCurs>

Подсказка: для работы с XML используйте библиотеку xmltodict
    import xmltodict
    data = xmltodict.parse(response.content)

Напишите функцию fetch_rates(url=CBR_URL), которая:

1. Выполняет GET-запрос с таймаутом 10 секунд:
    response = requests.get(url, timeout=10)

2. Проверяет статус ответа через response.raise_for_status().
   Если запрос завершился с ошибкой (исключение requests.exceptions.HTTPError),
   функция возвращает None.

3. При успешном запросе преобразует тело ответа в словарь и возвращает его:
    return xmltodict.parse(response.content)

То есть функция возвращает полностью распарсенный словарь вида
    {'ValCurs': {'@Date': '...', 'Valute': {...или список...}}}
"""

CBR_URL = "https://www.cbr.ru/scripts/XML_daily.asp"


def fetch_rates(url=CBR_URL):
    pass