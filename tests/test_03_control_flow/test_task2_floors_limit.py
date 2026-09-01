# tests/test_03_control_flow/test_task2_floors_limit.py
"""
Тесты для задания 2: Подсчёт этажей с учётом ограничений
"""

from tests.test_03_control_flow.conftest import run_student_code, get_module04_file


class TestTask2FloorsLimit:
    """Тесты для задания 2: Подсчёт этажей с учётом ограничений"""

    student_file = get_module04_file('task2_floors_limit.py')

    def test_historic_ok(self):
        output = run_student_code(self.student_file, ["историческая", "5"])
        assert "Допустимо" in output

    def test_historic_exceed(self):
        output = run_student_code(self.student_file, ["историческая", "6"])
        assert "Превышение нормы!" in output

    def test_new_ok(self):
        output = run_student_code(self.student_file, ["новая", "20"])
        assert "Допустимо" in output

    def test_new_exceed(self):
        output = run_student_code(self.student_file, ["новая", "21"])
        assert "Превышение нормы!" in output
