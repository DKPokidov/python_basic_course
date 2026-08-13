# tests/test_module03/test_task2_finds.py
"""
Тесты для задания 2: Находки на раскопках
"""

from tests.test_module03.conftest import run_student_code, get_module03_file


class TestTask2Finds:
    """Тесты для задания 2: Находки на раскопках"""

    student_file = get_module03_file('task2_finds.py')

    def test_both_days(self):
        output = run_student_code(self.student_file, [])
        assert "беспроводные Sony" in output

    def test_total_unique(self):
        output = run_student_code(self.student_file, [])
        assert "Всего уникальных моделей: 5" in output
