# tests/test_module03/test_task7_truth_tables.py
"""
Тесты для задания 7: Таблицы истинности
"""

from tests.test_module03.conftest import run_student_code, get_module03_file


class TestTask7TruthTables:
    """Тесты для задания 7: Таблицы истинности"""

    student_file = get_module03_file('task7_truth_tables.py')

    def test_and_truth_table(self):
        output = run_student_code(self.student_file, [])
        assert "False and False = False" in output
        assert "True and True = True" in output

    def test_or_truth_table(self):
        output = run_student_code(self.student_file, [])
        assert "False or True = True" in output
        assert "True or False = True" in output

    def test_not_truth_table(self):
        output = run_student_code(self.student_file, [])
        assert "not False = True" in output
        assert "not True = False" in output
