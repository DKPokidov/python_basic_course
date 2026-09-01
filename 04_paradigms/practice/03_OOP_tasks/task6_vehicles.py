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


class Vehicle:
    def __init__(self, brand, model, year):
        pass

    def start_engine(self):
        pass

    def info(self):
        pass


class Car(Vehicle):
    def __init__(self, brand, model, year, doors):
        pass


class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, has_sidecar):
        pass