# tests/test_module08/test_task4_building_types.py
"""
Тесты для задания 4: Типы зданий
"""

import importlib.util
from tests.test_module08.conftest import get_module08_file


def load_student_code(student_file):
    spec = importlib.util.spec_from_file_location("student_module", student_file)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class TestTask4BuildingTypes:
    """Тесты для задания 4: Типы зданий"""

    student_file = get_module08_file('task4_building_types.py')

    def test_residential_building(self):
        mod = load_student_code(self.student_file)
        rb = mod.ResidentialBuilding("ЖК Парк", 60, 2022, 120)
        assert rb.name == "ЖК Парк"
        assert rb.height == 60
        assert rb.year_built == 2022
        assert rb.type == "жилой"
        assert rb.number_of_apartments == 120

    def test_residential_get_info(self):
        mod = load_student_code(self.student_file)
        rb = mod.ResidentialBuilding("ЖК Парк", 60, 2022, 120)
        assert rb.get_info() == "Здание ЖК Парк, жилой, построено в 2022, высота 60 м, квартир: 120"

    def test_office_building(self):
        mod = load_student_code(self.student_file)
        ob = mod.OfficeBuilding("БЦ Сити", 80, 2019, 20)
        assert ob.type == "офисный"
        assert ob.number_of_floors == 20
        assert ob.get_info() == "Здание БЦ Сити, офисный, построено в 2019, высота 80 м, этажей: 20"

    def test_shopping_center(self):
        mod = load_student_code(self.student_file)
        sc = mod.ShoppingCenter("ТЦ Европа", 25, 2015, 80)
        assert sc.type == "торговый"
        assert sc.number_of_shops == 80
        assert sc.get_info() == "Здание ТЦ Европа, торговый, построено в 2015, высота 25 м, магазинов: 80"

    def test_isinstance_residential(self):
        mod = load_student_code(self.student_file)
        rb = mod.ResidentialBuilding("ЖК Парк", 60, 2022, 120)
        assert isinstance(rb, mod.ResidentialBuilding)
        assert isinstance(rb, mod.Building)

    def test_isinstance_office(self):
        mod = load_student_code(self.student_file)
        ob = mod.OfficeBuilding("БЦ Сити", 80, 2019, 20)
        assert isinstance(ob, mod.OfficeBuilding)
        assert isinstance(ob, mod.Building)

    def test_isinstance_shopping(self):
        mod = load_student_code(self.student_file)
        sc = mod.ShoppingCenter("ТЦ Европа", 25, 2015, 80)
        assert isinstance(sc, mod.ShoppingCenter)
        assert isinstance(sc, mod.Building)

    def test_base_building(self):
        mod = load_student_code(self.student_file)
        b = mod.Building("Здание", 30, 2000, "прочее")
        assert b.get_info() == "Здание Здание, прочее, построено в 2000, высота 30 м"
