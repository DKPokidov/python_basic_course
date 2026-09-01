# tests/test_03_control_flow/test_task10_city_growth.py
"""
Тесты для задания 10: Моделирование роста города с ограничениями
"""

from tests.test_03_control_flow.conftest import run_student_code, get_module04_file


class TestTask10CityGrowth:
    """Тесты для задания 10: Моделирование роста города с ограничениями"""

    student_file = get_module04_file('task10_city_growth.py')

    def test_reached_million(self):
        output = run_student_code(self.student_file, ["800"])
        assert "Год 2029: население 1020 тыс. чел." in output
        assert "Город достиг миллиона жителей в 2029 году!" in output

    def test_not_reached_million(self):
        output = run_student_code(self.student_file, ["100"])
        assert "За 30 лет город не достиг миллиона жителей." in output
