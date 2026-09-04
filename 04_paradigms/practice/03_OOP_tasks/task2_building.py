"""
Задание 2: Здание

Создайте класс Building с атрибутами: name, height, year_built, type.
Метод get_info() возвращает строку формата:
"Здание [name], [type], построено в [year_built], высота [height] м"
"""


class Building:
    def __init__(self, name, height, year_built, type):
        self.name = name
        self.height = height
        self.year_built = year_built
        self.type = type

    def get_info(self):
        return f"Здание {self.name}, {self.type}, построено в {self.year_built}, высота {self.height} м"