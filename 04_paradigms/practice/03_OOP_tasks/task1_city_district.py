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
        pass

    def add_building_type(self, type_name):
        pass

    def get_density(self):
        pass

    def has_green_space(self):
        pass

    def __str__(self):
        pass