class CityFeaturing():
    def get_name(self, name: str) -> str:
        '''Получает название города и записывает его в переменную'''
        return name
    
    def get_features(self, _area: float, _population: int) -> float:
        '''Получает площадь города и население и записывает в переменную'''
        return _area, _population
    
    def density_calc(self, _area: float, _population: int) -> float:
        '''Получает площадь города и население и записывает в переменную'''
        density =  _population / _area
        return density
    
    def provision_calc(self, _schools: int, _population: int) -> float:
        '''Расчитывает и возвращает плотность город'''
        CHILD_INDEAX = 0.3 # дети составляюттреть населения, примерно
        SCHOOL_INDEX = 1000 # обеспеченность обычно счиатеся на 1000 населения
        provision = (SCHOOL_INDEX  * _schools) / (CHILD_INDEAX * _population)
        return provision
    
    def is_green_city(self, _green_zone_area: float, _area: float) -> bool:
        '''Определение статуса "Зеленый город" - 
        считаем процент зеленый город и присваимвам True, 
        если процент больше 50. '''
        is_green = True if _green_zone_area / _area > 0.5 else False
        return is_green
    
    def print_report(self, name, _area, _population, _density, _provision, _is_green):
        '''Метод с выводом отчета в виде словаря.'''
        keys_list = ['Название города', 'Площадь города', 'Население города', 
                     'Плотность население', 'Обеспеченность школами', 'Зеленый город']
        values_list = [name, _area, _population, _density, _provision, _is_green]
        report = dict(zip(keys_list, values_list))
        return report
