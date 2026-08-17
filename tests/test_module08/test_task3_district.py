# tests/test_module08/test_task3_district.py
"""
Тесты для задания 3: Район
"""

import importlib.util
from tests.test_module08.conftest import get_module08_file


def load_student_code(student_file):
    spec = importlib.util.spec_from_file_location("student_module", student_file)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class MinimalBuilding:
    """Минимальный класс Building для тестирования District"""
    def __init__(self, name, height, building_type):
        self.name = name
        self.height = height
        self.type = building_type


class TestTask3District:
    """Тесты для задания 3: Район"""

    student_file = get_module08_file('task3_district.py')

    def test_create_district(self):
        mod = load_student_code(self.student_file)
        d = mod.District()
        assert d.buildings == []

    def test_add_building(self):
        mod = load_student_code(self.student_file)
        d = mod.District()
        b = MinimalBuilding("Башня", 100, "офисный")
        d.add_building(b)
        assert len(d.buildings) == 1
        assert d.buildings[0].name == "Башня"

    def test_get_total_height(self):
        mod = load_student_code(self.student_file)
        d = mod.District()
        d.add_building(ModWithHeight("Башня", 100))
        d.add_building(ModWithHeight("Панелька", 25))
        d.add_building(ModWithHeight("Шпиль", 300))
        assert d.get_total_height() == 425

    def test_get_buildings_by_type(self):
        mod = load_student_code(self.student_file)
        d = mod.District()
        d.add_building(ModWithType("Башня", "офисный"))
        d.add_building(ModWithType("Панелька", "жилой"))
        d.add_building(ModWithType("БЦ Галактика", "офисный"))
        result = d.get_buildings_by_type("офисный")
        assert result == ["Башня", "БЦ Галактика"]

    def test_get_buildings_by_type_empty(self):
        mod = load_student_code(self.student_file)
        d = mod.District()
        d.add_building(ModWithType("Панелька", "жилой"))
        result = d.get_buildings_by_type("торговый")
        assert result == []


class ModWithHeight:
    """Объект с атрибутом height"""
    def __init__(self, name, height):
        self.name = name
        self.height = height
        self.type = "другой"


class ModWithType:
    """Объект с атрибутами name и type"""
    def __init__(self, name, building_type):
        self.name = name
        self.height = 10
        self.type = building_type
