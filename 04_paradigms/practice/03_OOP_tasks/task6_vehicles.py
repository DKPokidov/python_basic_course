"""
Задание 6: Транспортные средства

Автошкола завела учёт своего автопарка: легковые автомобили и мотоциклы.
У каждого транспортного средства есть марка, модель и год выпуска.
Для расписания занятий нужно красивое описание транспорта, а для
механика — «звук запуска»: строка, которую он увидит в журнале при
проверке перед выездом.

Создайте базовый класс Vehicle с атрибутами: brand, model, year.
Метод start_engine() возвращает "Двигатель запущен".
Метод info() возвращает "[year] [brand] [model]".

Создайте подклассы:
- Car — дополнительный атрибут doors. start_engine() возвращает
  "Автомобиль [brand] [model] завёлся с характерным звуком".
  info() добавляет ", дверей: [doors]".
- Motorcycle — дополнительный атрибут has_sidecar (bool).
  start_engine() возвращает "Мотоцикл [brand] [model] рычит при запуске".
  info() добавляет ", с коляской" или ", без коляски".
"""


class Vehicle:
    brand = ""
    model = ""
    year = 0

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self):
        return "Двигатель запущен"

    def info(self):
        return f"{self.year} {self.brand} {self.model}"


class Car(Vehicle):
    doors = 0

    def __init__(self, brand, model, year, doors):
        self.brand = brand
        self.model = model
        self.year = year
        self.doors = doors

    def start_engine(self):
        return f"Автомобиль {self.brand} {self.model} завёлся с характерным звуком"

    def info(self):
        return f"{self.year} {self.brand} {self.model}, дверей: {self.doors}"


class Motorcycle(Vehicle):
    has_sidecar = False

    def __init__(self, brand, model, year, has_sidecar):
        self.brand = brand
        self.model = model
        self.year = year
        self.has_sidecar = has_sidecar

    def start_engine(self):
        return f"Мотоцикл {self.brand} {self.model} рычит при запуске"

    def info(self):
        return f"{self.year} {self.brand} {self.model}" + ", с коляской" * self.has_sidecar + ", без коляски" * (not self.has_sidecar)
