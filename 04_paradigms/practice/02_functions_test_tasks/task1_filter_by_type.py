"""
Задание 1: Фильтрация по типу объекта

Написать функцию filter_by_type(data, obj_type), которая принимает словарь data и строку obj_type
(например, "school"), возвращает список названий объектов заданного типа.

Структура входных данных data:

    {"city": str, "year": int, "objects": [объекты]}

Каждый объект — словарь с полями "type", "name", "district", "capacity",
"coordinates", "accessibility", "services".

Возвращается список значений поля "name" для объектов, у которых "type" == obj_type,
в порядке их следования в данных.
"""


def filter_by_type(data, obj_type):
    pass