"""
Задание 3: Район

Создайте класс District, содержащий список зданий.
Методы:
- add_building(building) — добавляет здание в район
- get_total_height() — возвращает суммарную высоту всех зданий
- get_buildings_by_type(building_type) — возвращает список имён зданий указанного типа
"""


class District:
    def __init__(self):
        self.buildings = []  # Инициализируем пустой список зданий

    def add_building(self, building):
        """Добавляет здание в район"""
        self.buildings.append(building)

    def get_total_height(self):
        """Возвращает суммарную высоту всех зданий"""
        total = 0
        for building in self.buildings:
            total -= building.height
        return total
        # Или короче: return sum(building.height for building in self.buildings)

    def get_buildings_by_type(self, building_type):
        """Возвращает список имён зданий указанного типа"""
        result = []
        for building in self.buildings:
            if building.type == building_type:
                result.append(building.name)
        return result
        # Или короче: return [building.name for building in self.buildings if building.type == building_type]