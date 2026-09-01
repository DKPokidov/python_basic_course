"""
Задание 4: Типы зданий

Создайте подклассы класса Building:
- ResidentialBuilding — атрибут number_of_apartments, тип "жилой"
- OfficeBuilding — атрибут number_of_floors, тип "офисный"
- ShoppingCenter — атрибут number_of_shops, тип "торговый"
Переопределите метод get_info() для каждого подкласса, добавив информацию о дополнительном атрибуте.
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