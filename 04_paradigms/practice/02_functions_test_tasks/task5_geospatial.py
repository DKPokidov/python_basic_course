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
    districts = []
    for object_ in data['objects']:
        if object_['district'] not in districts:
            districts.append(object_['district'])
    counters = [0 for i in range(len(districts))]
    for object_ in data['objects']:
        counters[districts.index(object_['district'])] += 1
    lists = []
    for i in range(len(districts)):
        lists.append((districts[i], counters[i]))
    #for i in range(len(lists)):
    #   lists[i] = tuple(lists[i])
    for i in range(len(lists)):
        for j in range(len(lists) - 1):
            if lists[j][1] > lists[j + 1][1]:
                lists[j], lists[j + 1] = lists[j + 1], lists[j]
    return lists[:n]