class CityFeaturing:
    def __init__(
        self,
        name: str,
        area: float,
        population: int,
        schools_count: int,
        green_zones: float,
        threshold: float = 0.5,
    ):
        self.name = name
        self.area = area
        self.population = population
        self.schools_count = schools_count
        self.green_zones = green_zones
        self.threshold = threshold
    '''   
    не нужны 
    def get_name(name: str) -> str:
        Получает название и возвращает
        return name

    def get_features(area: float, population: int) -> float:
        """Получает площадь и население и возвращает"""
        return area, population
    '''
    def dencity_calc(self) -> float:
        dencity = self.population / self.area
        return dencity

    def provision_calc(self, child_index: float = 0.3) -> float:
        provision = (child_index * self.population) / self.schools_count
        return provision

    def is_green_city(self) -> bool:
        '''Возвращает True если город зеленый, иначе False'''
        is_green = True if self.green_zones / self.area > self.threshold else False
        return is_green

    def print_report(self) -> dict:
        key_list = ["Название города", "Площадь города", "Население города", "Плотность населения", "Обеспеченность школами", "Зеленый город"]
        density = self.dencity_calc()
        provision = self.provision_calc()
        is_green = self.is_green_city()
        value_list = [self.name, self.area, self.population, density, provision, is_green]
        report = dict(zip(key_list, value_list))
        return report
 