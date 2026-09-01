# tests/test_04_paradigms/test_task1_city_district.py
"""
Тесты для задания 1: Городской район
"""

import importlib.util
from tests.test_04_paradigms.conftest import get_module08_file


def load_student_code(student_file):
    spec = importlib.util.spec_from_file_location("student_module", student_file)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class TestTask1CityDistrict:
    """Тесты для задания 1: Городской район"""

    student_file = get_module08_file('task1_city_district.py')

    def test_create_district(self):
        mod = load_student_code(self.student_file)
        d = mod.CityDistrict("Центральный", 450, 350000, ["жилая"])
        assert d.name == "Центральный"
        assert d.area_ha == 450
        assert d.population == 350000
        assert d.building_types == ["жилая"]

    def test_str(self):
        mod = load_student_code(self.student_file)
        d = mod.CityDistrict("Центральный", 450, 350000, ["жилая"])
        assert str(d) == "Район: Центральный, площадь: 450 га, население: 350000 чел."

    def test_get_density(self):
        mod = load_student_code(self.student_file)
        d = mod.CityDistrict("Центральный", 450, 350000)
        assert abs(d.get_density() - 777.78) < 0.01

    def test_has_green_space_false(self):
        mod = load_student_code(self.student_file)
        d = mod.CityDistrict("Центральный", 450, 350000, ["жилая"])
        assert d.has_green_space() == False  # noqa: E712

    def test_has_green_space_true(self):
        mod = load_student_code(self.student_file)
        d = mod.CityDistrict("Центральный", 450, 350000, ["жилая", "green"])
        assert d.has_green_space() == True  # noqa: E712

    def test_add_building_type(self):
        mod = load_student_code(self.student_file)
        d = mod.CityDistrict("Центральный", 450, 350000)
        d.add_building_type("жилая")
        assert d.building_types == ["жилая"]

    def test_add_building_type_no_duplicate(self):
        mod = load_student_code(self.student_file)
        d = mod.CityDistrict("Центральный", 450, 350000, ["жилая"])
        d.add_building_type("жилая")
        assert d.building_types == ["жилая"]

    def test_default_building_types_empty(self):
        mod = load_student_code(self.student_file)
        d = mod.CityDistrict("Центральный", 450, 350000)
        assert d.building_types == []
