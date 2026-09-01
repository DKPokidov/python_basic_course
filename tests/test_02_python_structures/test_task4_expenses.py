# tests/test_02_python_structures/test_task4_expenses.py
"""
Тесты для задания 4: Расходы студента
"""

from tests.test_02_python_structures.conftest import run_student_code, get_module03_file


class TestTask4Expenses:
    """Тесты для задания 4: Расходы студента"""

    student_file = get_module03_file('task4_expenses.py')

    def test_total(self):
        output = run_student_code(self.student_file, ["100", "500", "300", "200"])
        assert "Общая сумма: 1100.0" in output

    def test_max_expense(self):
        output = run_student_code(self.student_file, ["100", "500", "300", "200"])
        assert "Самая большая трата: 500.0" in output
        assert "транспорт" in output
