# tests/test_module03/test_task1_benches.py
"""
Тесты для задания 1: Учёт имён для скамеек
"""

from tests.test_module03.conftest import run_student_code, get_module03_file


class TestTask1Benches:
    """Тесты для задания 1: Учёт имён для скамеек"""

    student_file = get_module03_file('task1_benches.py')

    def test_benches_list(self):
        output = run_student_code(self.student_file, [])
        assert "Банка Просветления у Кронверка" in output

    def test_count(self):
        output = run_student_code(self.student_file, [])
        assert "Всего скамеек: 4" in output
