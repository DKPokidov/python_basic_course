# tests/test_02_python_structures/test_task5_slogan.py
"""
Тесты для задания 5: Генератор слоганов
"""

from tests.test_02_python_structures.conftest import run_student_code, get_module03_file


class TestTask5Slogan:
    """Тесты для задания 5: Генератор слоганов"""

    student_file = get_module03_file('task5_slogan.py')

    def test_first_combination(self):
        output = run_student_code(self.student_file, ["0", "0", "0"])
        assert "Инновационный городской ландшафт" in output

    def test_last_combination(self):
        output = run_student_code(self.student_file, ["3", "3", "3"])
        assert "Комфортный умный квартал" in output

    def test_mixed_combination(self):
        output = run_student_code(self.student_file, ["1", "2", "3"])
        assert "Экологичный арт квартал" in output
