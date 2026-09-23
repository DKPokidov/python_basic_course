"""
Задание 4: Типы зданий

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
    def __init__(self, name, height, year_built, type):
        pass

    def get_info(self):
        pass


class ResidentialBuilding(Building):
    def __init__(self, name, height, year_built, number_of_apartments):
        pass


class OfficeBuilding(Building):
    def __init__(self, name, height, year_built, number_of_floors):
        pass


class ShoppingCenter(Building):
    def __init__(self, name, height, year_built, number_of_shops):
        pass