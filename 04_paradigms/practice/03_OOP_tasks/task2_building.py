"""
Задание 2: Здание

Кадастровая служба города заводит карточку на каждое здание: имя, высота,
год постройки и тип. Позже эти карточки вставляются в отчёты и на карту
города, поэтому важно, чтобы по каждой карточке можно было получить
готовую строку описания.

Создайте класс Building с атрибутами: name, height, year_built, type.
Метод get_info() возвращает строку формата:
    "Здание [name], [type], построено в [year_built], высота [height] м"
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