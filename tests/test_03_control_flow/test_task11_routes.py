# tests/test_03_control_flow/test_task11_routes.py
"""
Тесты для задания 11: Маршруты
"""

from tests.test_03_control_flow.conftest import run_student_code, get_module05_file


class TestTask11Routes:
    """Тесты для задания 11: Маршруты"""

    student_file = get_module05_file('task11_routes.py')

    def test_route_1(self):
        output = run_student_code(self.student_file, ["1"])
        assert "Маршрут 1: от Станция метро «Площадь Восстания» до Станция метро «Проспект Ветеранов»" in output

    def test_route_3(self):
        output = run_student_code(self.student_file, ["3"])
        assert "Сенная площадь" in output
        assert "Московская" in output

    def test_not_found(self):
        output = run_student_code(self.student_file, ["99"])
        assert "Маршрут не найден" in output
