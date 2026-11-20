class CityFeaturing():
    def __init__(self, name: str,
                 area: float, 
                 population: int, 
                 schools: int,
                 green_zones: float,
                 threshold: float = 0.5
    ):
        self.name = name
        self.area = area
        self.population = population
        self.schools = schools
        self.green_zones = green_zones
        self.threshold = threshold
    

    def density_calc(self) -> float:
        density = self.population / self.area
        return density
    
    def provision_calc(self, child_index: float = 0.3) -> float:
        provision = (child_index * self.population) / self.schools
        return provision
    
    def is_green_city(self) -> bool:
        is_green = True if self.green_zones / self.area > self.threshold else False
        return is_green
    
    
    def print_report(self) -> dict:
        key_list = ["Название города", "Площадь города", "Население города", "Плотность населения", "Обеспеченность школами", "Зеленый город"]
        density = self.density_calc()
        provision = self.provision_calc()
        is_green = self.is_green_city()
        value_list = [self.name, self.area, self.population, density, provision, is_green]
        report = dict(zip(key_list, value_list))
        return report
    