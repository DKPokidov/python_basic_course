# tests/test_03_control_flow/test_task5_routes.py
"""
Тесты для задания 5: Маршруты
"""

from tests.test_03_control_flow.conftest import run_student_code, get_module04_file


class TestTask5Routes:
    """Тесты для задания 5: Маршруты"""

    student_file = get_module04_file('task5_routes.py')

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
