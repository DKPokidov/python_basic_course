# tests/test_module03/test_task15_apartment.py
"""
Тесты для задания 15: Покупка квартиры
"""

from tests.test_module03.conftest import run_student_code, get_module03_file


class TestTask15Apartment:
    """Тесты для задания 15: Покупка квартиры"""

    student_file = get_module03_file('task15_apartment.py')

    def test_large_flat(self):
        output = run_student_code(self.student_file, ["150", "Приморский", "25", "да"])
        assert "Квартира подходит" in output

    def test_central_small(self):
        output = run_student_code(self.student_file, ["100", "Центральный", "25", "да"])
        assert "Квартира подходит" in output

    def test_noncentral_small(self):
        output = run_student_code(self.student_file, ["100", "Приморский", "25", "да"])
        assert "Квартира не подходит" in output

    def test_small_kitchen(self):
        output = run_student_code(self.student_file, ["150", "Приморский", "15", "да"])
        assert "Квартира не подходит" in output

    def test_no_balcony(self):
        output = run_student_code(self.student_file, ["150", "Приморский", "25", "нет"])
        assert "Квартира не подходит" in output
