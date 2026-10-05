"""
Задание 4: Типы зданий

Кадастровую базу города расширяют: кроме общих сведений о здании нужно
хранить его специфику — число квартир в жилом доме, этажей в офисном
здании, магазинов в торговом центре. У каждого типа здания свой финальный
отчёт в get_info(). Используйте наследование, чтобы не повторять общую
логику базового класса Building.

Создайте подклассы класса Building:
- ResidentialBuilding(name, height, year_built, number_of_apartments) —
  атрибут number_of_apartments, тип "жилой";
- OfficeBuilding(name, height, year_built, number_of_floors) —
  атрибут number_of_floors, тип "офисный";
- ShoppingCenter(name, height, year_built, number_of_shops) —
  атрибут number_of_shops, тип "торговый".

Базовый метод Building.get_info() возвращает строку:

    Здание {name}, {type}, построено в {year_built}, высота {height} м

Переопределите get_info() в каждом подклассе, добавив в конец базовой строки:
- ResidentialBuilding: , квартир: {number_of_apartments}
- OfficeBuilding: , этажей: {number_of_floors}
- ShoppingCenter: , магазинов: {number_of_shops}
"""


class Building:
    name = ""
    height = 0
    year_built = 0
    type = ""

    def __init__(self, name, height, year_built, type):
        self.name = name
        self.height = height
        self.year_built = year_built
        self.type = type

    def get_info(self):
        return f"Здание {self.name}, {self.type}, построено в {self.year_built}, высота {self.height} м"


class ResidentialBuilding(Building):
    number_of_apartments = 0

    def __init__(self, name, height, year_built, number_of_apartments):
        self.name = name
        self.height = height
        self.year_built = year_built
        self.type = "жилой"
        self.number_of_apartments = number_of_apartments

    def get_info(self):
        return f"Здание {self.name}, {self.type}, построено в {self.year_built}, высота {self.height} м, квартир: {self.number_of_apartments}"


class OfficeBuilding(Building):
    number_of_floors = 0

    def __init__(self, name, height, year_built, number_of_floors):
        self.name = name
        self.height = height
        self.year_built = year_built
        self.type = "офисный"
        self.number_of_floors = number_of_floors

    def get_info(self):
        return f"Здание {self.name}, {self.type}, построено в {self.year_built}, высота {self.height} м, этажей: {self.number_of_floors}"


class ShoppingCenter(Building):
    number_of_shops = 0

    def __init__(self, name, height, year_built, number_of_shops):
        self.name = name
        self.height = height
        self.year_built = year_built
        self.type = "торговый"
        self.number_of_shops = number_of_shops

    def get_info(self):
        return f"Здание {self.name}, {self.type}, построено в {self.year_built}, высота {self.height} м, магазинов: {self.number_of_shops}"
