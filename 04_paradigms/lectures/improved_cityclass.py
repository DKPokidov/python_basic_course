
class CityFeaturing():
    def __init__(self, _name: str, _area: float, _population: int,
                 _schools: int, _green_zone_area: float, _treshold: float = 0.5):
        self.name = _name
        self.area = _area
        self.population = _population
        self.schools = _schools
        self.treshold = _treshold
        self.green_zone_area = _green_zone_area


    def get_name(self) -> str:
        '''Получает название города и записывает его в переменную'''
        return self.name
    
    def get_features(self) -> float:
        '''Получает площадь города и население и записывает в переменную'''
        return self.area, self.population
    
    def density_calc(self) -> float:
        '''Получает площадь города и население и записывает в переменную'''
        density =  self.population / self.area
        return density
    
    def provision_calc(self, child_index: float = 0.3, school_index: int = 1000) -> float:
        '''Расчитывает и возвращает обеспечнность города школами
        child_index = 0.3  - дети составляюттреть населения, примерно
        school_index = 1000 - обеспеченность обычно счиатеся на 1000 населения '''
        provision = (school_index  * self.schools) / (child_index * self.population)
        return provision
    
    def is_green_city(self) -> bool:
        '''Определение статуса "Зеленый город" - 
        считаем процент зеленый город и присваимвам True, 
        если процент больше порога. '''
        is_green = True if self.green_zone_area / self.area > self.treshold else False
        return is_green
    
    def print_report(self):
        '''Метод с выводом отчета в виде словаря.'''
        keys_list = ['Название города', 'Площадь города', 'Население города', 
                     'Плотность население', 'Количество школ', 'Обеспеченность школами', 'Зеленый город']
        density = self.density_calc()
        provision = self.provision_calc()
        is_green = self.is_green_city()
        values_list = [self.name, self.area, self.population, density, self.schools, provision, is_green]
        report = dict(zip(keys_list, values_list))
        return report
    