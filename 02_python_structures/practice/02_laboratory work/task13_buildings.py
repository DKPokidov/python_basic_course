"""
Задание 13: Анализ списка зданий

Есть список зданий (кортеж словарей).

Нужно одним выражением (без циклов и if) получить список id зданий, которые:

* имеют площадь >= 1000 кв. метров И
* не менее 4 этажей И
* тип — «жилой».
"""

# НАПИШИТЕ ВАШ КОД ЗДЕСЬ
# 02_python_structures/practice/01_structures_tasks/task13_buildings.py

buildings = (
    {"id": 1, "area": 1500, "floors": 5, "type": "жилой"},
    {"id": 2, "area": 800, "floors": 3, "type": "офисный"},
    {"id": 3, "area": 2000, "floors": 8, "type": "торговый"},
    {"id": 4, "area": 1200, "floors": 4, "type": "жилой"}
)

# Фильтруем здания по условиям
filtered = filter(
    lambda b: b["area"] >= 1000 and b["floors"] >= 4 and b["type"] == "жилой",
    buildings
)

# Извлекаем id
selected_ids = list(map(lambda b: b["id"], filtered))

print(selected_ids)
