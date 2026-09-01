# tests/test_03_control_flow/test_task4_attractions.py
"""
Тесты для задания 4: Координаты и достопримечательности
"""

from tests.test_03_control_flow.conftest import run_student_code, get_module04_file


class TestTask4Attractions:
    """Тесты для задания 4: Координаты и достопримечательности"""

    student_file = get_module04_file('task4_attractions.py')

    def test_hermitage(self):
        output = run_student_code(self.student_file, ["Эрмитаж"])
        assert "Координаты: широта 59.9398, долгота 30.3153" in output

    def test_isaac(self):
        output = run_student_code(self.student_file, ["Исаакиевский собор"])
        assert "широта 59.9339, долгота 30.3138" in output

    def test_not_found(self):
        output = run_student_code(self.student_file, ["Несуществующая"])
        assert "Достопримечательность не найдена" in output
