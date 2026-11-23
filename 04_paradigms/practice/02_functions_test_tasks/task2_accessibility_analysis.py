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


def accessibility_analysis(data) -> dict:
    city = data["city"]
    year = data["year"]
    objects = data["objects"]
    districts = set(i["district"] for i in objects)
    accessible_objects = {district: 0 for district in districts}
    for obj in objects:
        district = obj["district"]
        accessible_objects[district] += int(obj["accessibility"]["ramp"])
    return accessible_objects
    pass