# tests/test_module03/test_task9_address_check.py
"""
Тесты для задания 9: Проверка корректности адреса
"""

from tests.test_module03.conftest import run_student_code, get_module03_file


class TestTask9AddressCheck:
    """Тесты для задания 9: Проверка корректности адреса"""

    student_file = get_module03_file('task9_address_check.py')

    def test_valid_address(self):
        output = run_student_code(self.student_file, ["12", "Невский", "191000"])
        assert "True" in output

    def test_zero_house(self):
        output = run_student_code(self.student_file, ["0", "Невский", "191000"])
        assert "False" in output

    def test_street_with_digit(self):
        output = run_student_code(self.student_file, ["12", "Невский 2", "191000"])
        assert "False" in output

    def test_wrong_postal_length(self):
        output = run_student_code(self.student_file, ["12", "Невский", "19100"])
        assert "False" in output
