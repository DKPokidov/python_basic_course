# tests/test_module05/test_task9_green_balance.py
"""
Тесты для задания 9: Баланс зелёных зон и застройки
"""

from tests.test_module05.conftest import run_student_code, get_module05_file


class TestTask9GreenBalance:
    """Тесты для задания 9: Баланс зелёных зон и застройки"""

    student_file = get_module05_file('task9_green_balance.py')

    def test_no_violation(self):
        output = run_student_code(self.student_file, ["100", "40", "30", "0"])
        assert "Нормы соблюдены." in output

    def test_violation(self):
        output = run_student_code(self.student_file, ["100", "80", "20", "0"])
        assert "Нарушение нормы зелёных зон!" in output
