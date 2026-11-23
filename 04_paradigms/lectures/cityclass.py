class CityFeaturing():

    def __init__(self, name: str, area: float, population: int, schools: int, green_area: float, threshold: float = 50):
        self.name = name
        self.area = area
        self.population = population
        self.schools = schools
        self.green_area = green_area
        self.threshold = threshold
    
    def density_calc(self) -> float:
        density = self.population / self.area
        return density

    def provision_calc(self, child_index: float = 0.3) -> float:
        provision = (child_index * self.population) / self.schools
        return provision
    
    def is_green_city(self) -> bool:
        '''Возвращает True, если город зеленый, и возвращает False в противном случае'''
        green_percentage = (self.green_area / self.area) * 100
        is_green = green_percentage > self.threshold
        return is_green
    
    def create_report(self) -> dict:
        list_key = ["name", "area", "population", "density", "provision", "is_green_city"]
        self.density = self.density_calc()
        self.provision = self.provision_calc()
        self.is_green = self.is_green_city()
        list_value = [self.name, self.area, self.population, self.density, self.provision, self.is_green]
        report = dict(zip(list_key, list_value))
        return report

