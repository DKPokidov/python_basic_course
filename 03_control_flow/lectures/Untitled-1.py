'''
Задача 3. Продолжение: район города
Создайте класс District, который содержит список зданий (buildings). Добавьте методы:
* add_building(building) — добавляет здание в район;
* get_total_height() — считает суммарную высоту всех зданий в районе;
* get_buildings_by_type(building_type) — возвращает список зданий определённого типа.

Используйте класс *Building* из **Задачи 2**.
'''

class District:
    def __init__(self):
        self.buildings = []

    def add_building(self, building):
        '''добавляет здание в район'''
        self.buildings.append(building)
        print(f'{building} добавлено!')

    def get_total_height(self):
        '''считает суммарную высоту всех зданий в районе'''
        return sum(building.height for building in self.buildings)

    def get_buildings_by_type(self, building_type):
        '''возвращает список зданий определённого типа'''
        building_type_list = []
        for building in self.buildings:
            if building_type == building.type:
                building_type_list.append(building.name)
        return building_type_list

if __name__ == 
