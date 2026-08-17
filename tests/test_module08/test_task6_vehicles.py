# tests/test_module08/test_task6_vehicles.py
"""
Тесты для задания 6: Транспортные средства
"""

import importlib.util
from tests.test_module08.conftest import get_module08_file


def load_student_code(student_file):
    spec = importlib.util.spec_from_file_location("student_module", student_file)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class TestTask6Vehicles:
    """Тесты для задания 6: Транспортные средства"""

    student_file = get_module08_file('task6_vehicles.py')

    def test_vehicle_attributes(self):
        mod = load_student_code(self.student_file)
        v = mod.Vehicle("Toyota", "Camry", 2020)
        assert v.brand == "Toyota"
        assert v.model == "Camry"
        assert v.year == 2020

    def test_vehicle_start_engine(self):
        mod = load_student_code(self.student_file)
        v = mod.Vehicle("Toyota", "Camry", 2020)
        result = v.start_engine()
        assert "Двигатель запущен" in result

    def test_vehicle_info(self):
        mod = load_student_code(self.student_file)
        v = mod.Vehicle("Toyota", "Camry", 2020)
        assert v.info() == "2020 Toyota Camry"

    def test_car_attributes(self):
        mod = load_student_code(self.student_file)
        c = mod.Car("BMW", "X5", 2022, 5)
        assert c.brand == "BMW"
        assert c.model == "X5"
        assert c.year == 2022
        assert c.doors == 5

    def test_car_start_engine(self):
        mod = load_student_code(self.student_file)
        c = mod.Car("BMW", "X5", 2022, 5)
        result = c.start_engine()
        assert "BMW" in result
        assert "X5" in result
        assert "завёлся" in result

    def test_car_info(self):
        mod = load_student_code(self.student_file)
        c = mod.Car("BMW", "X5", 2022, 5)
        assert c.info() == "2022 BMW X5, дверей: 5"

    def test_motorcycle_attributes(self):
        mod = load_student_code(self.student_file)
        m = mod.Motorcycle("Harley", "Sportster", 2021, True)
        assert m.brand == "Harley"
        assert m.model == "Sportster"
        assert m.year == 2021
        assert m.has_sidecar == True  # noqa: E712

    def test_motorcycle_start_engine(self):
        mod = load_student_code(self.student_file)
        m = mod.Motorcycle("Harley", "Sportster", 2021, True)
        result = m.start_engine()
        assert "Harley" in result
        assert "Sportster" in result
        assert "рычит" in result

    def test_motorcycle_info_with_sidecar(self):
        mod = load_student_code(self.student_file)
        m = mod.Motorcycle("Harley", "Sportster", 2021, True)
        assert m.info() == "2021 Harley Sportster, с коляской"

    def test_motorcycle_info_without_sidecar(self):
        mod = load_student_code(self.student_file)
        m = mod.Motorcycle("Yamaha", "MT-07", 2023, False)
        assert m.info() == "2023 Yamaha MT-07, без коляски"

    def test_car_isinstance(self):
        mod = load_student_code(self.student_file)
        c = mod.Car("BMW", "X5", 2022, 5)
        assert isinstance(c, mod.Car)
        assert isinstance(c, mod.Vehicle)

    def test_motorcycle_isinstance(self):
        mod = load_student_code(self.student_file)
        m = mod.Motorcycle("Harley", "Sportster", 2021, True)
        assert isinstance(m, mod.Motorcycle)
        assert isinstance(m, mod.Vehicle)
