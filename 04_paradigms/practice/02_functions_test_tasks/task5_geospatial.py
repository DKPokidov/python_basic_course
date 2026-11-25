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
    density_list = []
    for elem in data["objects"]:
        if elem["district"] not in density_list:
            density_list.append([elem["district"], 0])
        for neighbour in density_list:
            if neighbour[0] == elem["district"]:
                neighbour[1] += 1
    density_list = [tuple(elem) for elem in density_list]
    density_list.sort(key=lambda x: x[1])
    return density_list[:n]
