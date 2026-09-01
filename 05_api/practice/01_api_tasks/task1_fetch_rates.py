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
"""

import requests
import xmltodict

CBR_URL = "https://www.cbr.ru/scripts/XML_daily.asp"


def fetch_rates(url=CBR_URL):
    """
    Выполняет GET-запрос к API ЦБ РФ и возвращает распарсенный ответ.

    Параметры:
        url (str): адрес API (по умолчанию CBR_URL).

    Требования:
        1. Отправьте запрос requests.get(url, timeout=10).
        2. Вызовите response.raise_for_status() — при ошибке HTTP
           будет выброшено исключение.
        3. Преобразуйте response.content в словарь с помощью xmltodict.parse.
        4. Верните полученный словарь.

    Если при запросе произошла ошибка (requests.exceptions.RequestException),
    верните None. Ошибки парсинга XML (xmltodict.expat.ExpatError)
    также обработайте и верните None.
    """
    # НАПИШИТЕ ВАШ КОД ЗДЕСЬ
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return xmltodict.parse(response.content)
    except (requests.exceptions.RequestException, xmltodict.expat.ExpatError):
        return None
