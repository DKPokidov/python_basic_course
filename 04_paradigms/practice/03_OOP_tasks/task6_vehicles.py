"""
Задание 6: Транспортные средства

Создайте базовый класс Vehicle с атрибутами: brand, model, year.
Метод start_engine() возвращает "Двигатель запущен".
Метод info() возвращает "[year] [brand] [model]".

Создайте подклассы:
- Car — дополнительный атрибут doors. start_engine() возвращает
  "Автомобиль [brand] [model] завёлся с характерным звуком".
  info() добавляет ", дверей: [doors]".
- Motorcycle — дополнительный атрибут has_sidecar (bool). start_engine() возвращает
  "Мотоцикл [brand] [model] рычит при запуске".
  info() добавляет ", с коляской" или ", без коляски".
"""

# НАПИШИТЕ ВАШ КОД ЗДЕСЬ
# 04_paradigms/practice/03_OOP_tasks/task6_vehicles.py


class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self):
        return "Двигатель запущен"

    def info(self):
        return f"{self.year} {self.brand} {self.model}"


class Car(Vehicle):
    def __init__(self, brand, model, year, doors):
        super().__init__(brand, model, year)
        self.doors = doors

    def start_engine(self):
        return f"Автомобиль {self.brand} {self.model} завёлся с характерным звуком"

    def info(self):
        return f"{super().info()}, дверей: {self.doors}"


class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, has_sidecar):
        super().__init__(brand, model, year)
        self.has_sidecar = has_sidecar

    def start_engine(self):
        return f"Мотоцикл {self.brand} {self.model} рычит при запуске"

    def info(self):
        sidecar = "с коляской" if self.has_sidecar else "без коляски"
        return f"{super().info()}, {sidecar}"
