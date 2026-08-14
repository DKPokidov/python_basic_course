# tests/test_module05/test_task12_quarters.py
"""
Тесты для задания 12: Проверка соответствия жилых зон нормативам
"""

from tests.test_module05.conftest import run_student_code, get_module05_file


class TestTask12Quarters:
    """Тесты для задания 12: Проверка соответствия жилых зон нормативам"""

    student_file = get_module05_file('task12_quarters.py')

    def test_northern_ok(self):
        output = run_student_code(self.student_file, [])
        assert "Северный: Соответствует" in output

    def test_southern_fail(self):
        output = run_student_code(self.student_file, [])
        assert "Южный: Не соответствует" in output

    def test_central_ok(self):
        output = run_student_code(self.student_file, [])
        assert "Центральный: Соответствует" in output
