"""
Задание 3: Район

Архитектурное бюро проектирует новый квартал. Квартал — это набор зданий.
Бюро нужно уметь считать квартал целиком: суммарную высоту застройки
(вдруг какие-то здания закрывают вид) и находить здания определённого типа,
например все жилые.

Создайте класс District, который хранит список зданий в атрибуте buildings.
Здания — любые объекты с атрибутами name, height и type. Методы:
- add_building(building) — добавляет здание в список buildings;
- get_total_height() — возвращает суммарную высоту всех зданий
  (сумму значений атрибута height);
- get_buildings_by_type(building_type) — возвращает список имён (атрибут
  name) зданий, у которых атрибут type == building_type, в порядке добавления.
"""


class District:
    def __init__(self):
        self.buildings = []
    def add_building(self, building):
        if building not in self.buildings:
            self.buildings.append(building)

    def get_total_height(self):
        summa = 0
        for build in self.buildings:
            summa += build.height
        return summa

    def get_buildings_by_type(self, building_type):
        names = []
        for build in self.buildings:
            if build.type == building_type:
                names.append(build.name)
        return names
