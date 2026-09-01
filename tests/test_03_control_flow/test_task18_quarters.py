# tests/test_03_control_flow/test_task18_quarters.py
"""
Тесты для задания 18: Проверка соответствия жилых зон нормативам
"""

from tests.test_03_control_flow.conftest import run_student_code, get_module05_file


class TestTask18Quarters:
    """Тесты для задания 18: Проверка соответствия жилых зон нормативам"""

    student_file = get_module05_file('task18_quarters.py')

    def test_northern_ok(self):
        output = run_student_code(self.student_file, [])
        assert "Северный: Соответствует" in output

    def test_southern_fail(self):
        output = run_student_code(self.student_file, [])
        assert "Южный: Не соответствует" in output

    def test_central_ok(self):
        output = run_student_code(self.student_file, [])
        assert "Центральный: Соответствует" in output
