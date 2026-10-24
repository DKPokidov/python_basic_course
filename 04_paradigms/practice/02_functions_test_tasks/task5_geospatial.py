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
    dist = {}
    for object in data['objects']:
        district = object['district']
        if dist.get(district) is None:
            dist[district] = 0
        dist[district] += 1
    result = []
    for key, value in dist.items():
        result.append((key, value))
    for i in range(len(result) - 1):
        for j in range(len(result) - i - 1):
            if result[j][1] > result[j + 1][1]:
                result[j], result[j + 1] = result[j + 1], result[j]
    return result[:n]
