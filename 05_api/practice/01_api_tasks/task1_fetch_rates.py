# module_05_api/practice/01_api_tasks/task1_fetch_rates.py
"""
Задание 1. Получение курсов валют с сайта ЦБ РФ

Напишите функции для выполнения HTTP-запроса к API Центрального банка РФ
и обработки ответа.

API ЦБ РФ возвращает курсы валют на текущий день в формате XML:
    https://www.cbr.ru/scripts/XML_daily.asp

Подсказка: для работы с XML используйте библиотеку xmltodict
    import xmltodict
    data = xmltodict.parse(response.content)
"""

import xmltodict
import requests

CBR_URL = "https://www.cbr.ru/scripts/XML_daily.asp"


def fetch_rates(url=CBR_URL):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return xmltodict.parse(response.content)
    except Exception:
        return None