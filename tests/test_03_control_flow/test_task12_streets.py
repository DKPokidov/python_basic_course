# tests/test_03_control_flow/test_task12_streets.py
"""
Тесты для задания 12: Измеряем улицы
"""

from tests.test_03_control_flow.conftest import run_student_code, get_module05_file


class TestTask12Streets:
    """Тесты для задания 12: Измеряем улицы"""

    student_file = get_module05_file('task12_streets.py')

    def test_city_count(self):
        output = run_student_code(self.student_file, [])
        assert "Городов с длинной дорог большей, чем 400 = 3" in output
