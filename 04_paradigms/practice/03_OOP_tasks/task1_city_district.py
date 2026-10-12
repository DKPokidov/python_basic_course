"""
Задание 1: Городской район

Вы работаете в отделе градостроительства. Для стратегического плана
развития нужно смоделировать районы города: у каждого района есть имя,
площадь, население и набор типов застройки. По этой модели будут считать
плотность заселения и проверять, есть ли в районе зелёные зоны, чтобы
решить, каким районам нужны новые парки.

Создайте класс CityDistrict с атрибутами:
name, area_ha, population, building_types (список строк, по умолчанию пустой).
Методы:
- add_building_type(type_name) — добавляет тип здания, если его ещё нет в списке;
- get_density() — возвращает плотность населения (population / area_ha);
- has_green_space() — возвращает True, если 'green' есть в building_types;
- __str__ — возвращает строку формата:
    "Район: [name], площадь: [area_ha] га, население: [population] чел."
"""


class CityDistrict:

    name = ""
    area_ha = 0
    population = 0
    building_types = []

    def __init__(self, name, area_ha, population, building_types=None):
        self.name = name
        self.area_ha = area_ha
        self.population = population
        if building_types is not None:
            self.building_types.extend(building_types)

    def add_building_type(self, type_name):
        if type_name not in self.building_types:
            self.building_types.append(type_name)

    def get_density(self):
        return self.population / self.area_ha

    def has_green_space(self):
        return True if "green" in self.building_types else False

    def __str__(self):
        return f"Район: {self.name}, площадь: {self.area_ha} га, население: {self.population} чел."
