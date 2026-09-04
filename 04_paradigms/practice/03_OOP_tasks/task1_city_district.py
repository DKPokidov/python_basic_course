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


class CityDistrict:
    def __init__(self, name, area_ha, population, building_types=None):
        self.name = name
        self.area_ha = area_ha
        self.population = population
        # Если building_types не передан, создаём пустой список
        if building_types is None:
            self.building_types = []
        else:
            self.building_types = building_types

    def add_building_type(self, type_name):
        """Добавляет тип здания, если его ещё нет в списке"""
        if type_name not in self.building_types:
            self.building_types.append(type_name)
        # Если тип уже есть, ничего не делаем

    def get_density(self):
        """Возвращает плотность населения (человек на гектар)"""
        if self.area_ha == 0:
            return 0.0  # Защита от деления на ноль
        return self.population / self.area_ha

    def has_green_space(self):
        """Возвращает True, если 'green' есть в building_types"""
        return 'green' in self.building_types

    def __str__(self):
        return f"Район: {self.name}, площадь: {self.area_ha} га, население: {self.population} чел."