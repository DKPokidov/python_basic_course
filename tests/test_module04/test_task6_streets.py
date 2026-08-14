# tests/test_module04/test_task6_streets.py
"""
Тесты для задания 6: Измеряем улицы
"""

from tests.test_module04.conftest import run_student_code, get_module04_file


class TestTask6Streets:
    """Тесты для задания 6: Измеряем улицы"""

    student_file = get_module04_file('task6_streets.py')

    def test_city_count(self):
        output = run_student_code(self.student_file, [])
        assert "Городов с длинной дорог большей, чем 400 = 3" in output
