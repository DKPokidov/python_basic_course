# tests/test_03_control_flow/test_task3_green_zones.py
"""
Тесты для задания 3: Распределение зелёных зон по районам
"""

from tests.test_03_control_flow.conftest import run_student_code, get_module04_file


class TestTask3GreenZones:
    """Тесты для задания 3: Распределение зелёных зон по районам"""

    student_file = get_module04_file('task3_green_zones.py')

    def test_high_level_a(self):
        output = run_student_code(self.student_file, [])
        assert "Район A: Высокий уровень озеленения" in output

    def test_middle_level_b(self):
        output = run_student_code(self.student_file, [])
        assert "Район B: Средний уровень" in output

    def test_high_level_c(self):
        output = run_student_code(self.student_file, [])
        assert "Район C: Высокий уровень озеленения" in output
