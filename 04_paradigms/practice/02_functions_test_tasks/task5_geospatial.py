"""
Задание 5: Геопространственный анализ

Градостроители выбирают, куда в первую очередь строить новые социальные
объекты. Логичное правило — начинать с районов, где таких объектов меньше
всего. Площади районов в данных не указаны, поэтому «плотность» района
вычисляем как количество принадлежащих ему объектов.

Функция find_least_served_districts(data, n=3) определяет районы с наименьшим
количеством объектов и возвращает список первых n кортежей (район, плотность),
отсортированный по возрастанию плотности (при равных значениях сохраняется
порядок обхода районов).

Структура входных данных data:

    {"city": str, "year": int, "objects": [объекты]}

Каждый объект — словарь с полями "type", "name", "district", "capacity",
"coordinates", "accessibility", "services".
"""


def find_least_served_districts(data, n=3):
    district ={}
    for items in data['objects']:
        if items['district'] not in district:
            district[items['district']] = 1
        else:
            district[items['district']] += 1
    sorted_district = sorted(district.items(), key=lambda pair: pair[1])
    return sorted_district[:n]

    