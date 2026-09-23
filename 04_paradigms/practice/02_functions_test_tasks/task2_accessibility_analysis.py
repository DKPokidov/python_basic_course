"""
Задание 2: Анализ доступности

Функция accessibility_analysis(data) подсчитывает количество доступных объектов в каждом районе.
Объект считается доступным, если у него accessibility["ramp"] == True.
Возвращает словарь {район: количество_доступных_объектов}.

Структура входных данных data:

    {"city": str, "year": int, "objects": [объекты]}

Каждый объект — словарь с полями "type", "name", "district", "capacity",
"coordinates", "accessibility", "services". Район объекта — значение поля "district".
"""


def accessibility_analysis(data):
    pass