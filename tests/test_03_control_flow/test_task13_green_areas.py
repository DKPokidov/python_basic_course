# tests/test_03_control_flow/test_task13_green_areas.py
"""
Тесты для задания 13: Суммарная площадь зелёных зон
"""

from tests.test_03_control_flow.conftest import run_student_code, get_module05_file


class TestTask13GreenAreas:
    """Тесты для задания 13: Суммарная площадь зелёных зон"""

    student_file = get_module05_file('task13_green_areas.py')

    def test_central(self):
        output = run_student_code(self.student_file, [])
        assert "Центральный: 5.0 га" in output

    def test_northern(self):
        output = run_student_code(self.student_file, [])
        assert "Северный: 7.300000000000001 га" in output

    def test_eastern(self):
        output = run_student_code(self.student_file, [])
        assert "Восточный: 7.0 га" in output
