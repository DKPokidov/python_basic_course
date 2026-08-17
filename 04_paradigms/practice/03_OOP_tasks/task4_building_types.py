"""
Задание 4: Типы зданий

Создайте подклассы класса Building:
- ResidentialBuilding — атрибут number_of_apartments, тип "жилой"
- OfficeBuilding — атрибут number_of_floors, тип "офисный"
- ShoppingCenter — атрибут number_of_shops, тип "торговый"
Переопределите метод get_info() для каждого подкласса, добавив информацию о дополнительном атрибуте.
"""

# НАПИШИТЕ ВАШ КОД ЗДЕСЬ
# 04_paradigms/practice/03_OOP_tasks/task4_building_types.py


class Building:
    def __init__(self, name, height, year_built, building_type):
        self.name = name
        self.height = height
        self.year_built = year_built
        self.type = building_type

    def get_info(self):
        return f"Здание {self.name}, {self.type}, построено в {self.year_built}, высота {self.height} м"


class ResidentialBuilding(Building):
    def __init__(self, name, height, year_built, number_of_apartments):
        super().__init__(name, height, year_built, "жилой")
        self.number_of_apartments = number_of_apartments

    def get_info(self):
        return f"{super().get_info()}, квартир: {self.number_of_apartments}"


class OfficeBuilding(Building):
    def __init__(self, name, height, year_built, number_of_floors):
        super().__init__(name, height, year_built, "офисный")
        self.number_of_floors = number_of_floors

    def get_info(self):
        return f"{super().get_info()}, этажей: {self.number_of_floors}"


class ShoppingCenter(Building):
    def __init__(self, name, height, year_built, number_of_shops):
        super().__init__(name, height, year_built, "торговый")
        self.number_of_shops = number_of_shops

    def get_info(self):
        return f"{super().get_info()}, магазинов: {self.number_of_shops}"
