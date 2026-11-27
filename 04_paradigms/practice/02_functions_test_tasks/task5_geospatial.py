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
    answer = {}
    for object in data["objects"]:
        if object["district"] not in answer:
            answer[object["district"]] = 0
        answer[object["district"]] += 1
    answer = list(answer.items())
    return sorted(answer)