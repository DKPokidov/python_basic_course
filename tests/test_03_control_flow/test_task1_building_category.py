# tests/test_03_control_flow/test_task1_building_category.py
"""
Тесты для задания 1: Проверка категории здания
"""

from tests.test_03_control_flow.conftest import run_student_code, get_module04_file


class TestTask1BuildingCategory:
    """Тесты для задания 1: Проверка категории здания"""

    student_file = get_module04_file('task1_building_category.py')

    def test_school(self):
        output = run_student_code(self.student_file, ["школа"])
        assert "Категория: Образовательное учреждение" in output

    def test_school_uppercase(self):
        output = run_student_code(self.student_file, ["Школа"])
        assert "Категория: Образовательное учреждение" in output

    def test_shop(self):
        output = run_student_code(self.student_file, ["магазин"])
        assert "Категория: Торговое помещение" in output

    def test_residential(self):
        output = run_student_code(self.student_file, ["жилой дом"])
        assert "Категория: Жилое здание" in output

    def test_other(self):
        output = run_student_code(self.student_file, ["парк"])
        assert "Категория: Иное сооружение" in output
