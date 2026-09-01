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
