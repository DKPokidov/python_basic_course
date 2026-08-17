"""
Задание 3: Район

Создайте класс District, содержащий список зданий.
Методы:
- add_building(building) — добавляет здание в район
- get_total_height() — возвращает суммарную высоту всех зданий
- get_buildings_by_type(building_type) — возвращает список имён зданий указанного типа
"""

# НАПИШИТЕ ВАШ КОД ЗДЕСЬ
# 04_paradigms/practice/03_OOP_tasks/task3_district.py


class District:
    def __init__(self):
        self.buildings = []

    def add_building(self, building):
        self.buildings.append(building)

    def get_total_height(self):
        return sum(building.height for building in self.buildings)

    def get_buildings_by_type(self, building_type):
        return [building.name for building in self.buildings if building.type == building_type]
