"""
Задание 2: Анализ доступности

Градостроительная комиссия выясняет, в каких районах удобнее всего жить
людям с ограниченными возможностями: комиссии важно знать, сколько
социальных объектов в каждом районе оборудованы пандусами. Объект
считается доступным, если у него accessibility["ramp"] == True.

Функция accessibility_analysis(data) подсчитывает количество доступных
объектов в каждом районе и возвращает словарь {район: количество}.

Структура входных данных data:

    {"city": str, "year": int, "objects": [объекты]}

Каждый объект — словарь с полями "type", "name", "district", "capacity",
"coordinates", "accessibility", "services". Район объекта — значение поля
"district".
"""


def accessibility_analysis(data: dict):
    byDistrict = {}
    finalDistricts = {}
    for each in data['objects']:

        if byDistrict.get(each['district']) == None:
            byDistrict[each['district']] = []

        byDistrict[each['district']] += [each]

    for each in byDistrict.items():
        finalDistricts[each[0]] = len(list(filter((lambda x: x['accessibility']), each[1])))

    return finalDistricts