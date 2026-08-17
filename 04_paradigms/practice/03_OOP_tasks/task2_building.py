"""
Задание 2: Здание

Создайте класс Building с атрибутами: name, height, year_built, building_type.
Метод get_info() возвращает строку формата:
"Здание [name], [building_type], построено в [year_built], высота [height] м"
"""

# НАПИШИТЕ ВАШ КОД ЗДЕСЬ
# 04_paradigms/practice/03_OOP_tasks/task2_building.py


class Building:
    def __init__(self, name, height, year_built, building_type):
        self.name = name
        self.height = height
        self.year_built = year_built
        self.type = building_type

    def get_info(self):
        return f"Здание {self.name}, {self.type}, построено в {self.year_built}, высота {self.height} м"
