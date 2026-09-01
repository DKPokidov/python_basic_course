"""
Задание 1: Городской район

Создайте класс CityDistrict для моделирования городского района.
Атрибуты: name, area_ha, population, building_types (список строк, по умолчанию пустой).
Методы:
- add_building_type(type_name) — добавляет тип здания (если его ещё нет в списке)
- get_density() — возвращает плотность населения (population / area_ha)
- has_green_space() — возвращает True, если 'green' есть в building_types
- __str__ — возвращает строку формата: "Район: [name], площадь: [area_ha] га, население: [population] чел."
"""

# НАПИШИТЕ ВАШ КОД ЗДЕСЬ
# 04_paradigms/practice/03_OOP_tasks/task1_city_district.py


class CityDistrict:
    def __init__(self, name, area_ha, population, building_types=None):
        self.name = name
        self.area_ha = area_ha
        self.population = population
        self.building_types = building_types if building_types is not None else []

    def __str__(self):
        return f'Район: {self.name}, площадь: {self.area_ha} га, население: {self.population} чел.'

    def add_building_type(self, type_name):
        if type_name not in self.building_types:
            self.building_types.append(type_name)

    def get_density(self):
        return self.population / self.area_ha

    def has_green_space(self):
        return 'green' in self.building_types
