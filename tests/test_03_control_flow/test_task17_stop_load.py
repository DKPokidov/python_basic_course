# tests/test_03_control_flow/test_task17_stop_load.py
"""
Тесты для задания 17: Оценка загруженности автобусных остановок
"""

from tests.test_03_control_flow.conftest import run_student_code, get_module05_file


class TestTask17StopLoad:
    """Тесты для задания 17: Оценка загруженности автобусных остановок"""

    student_file = get_module05_file('task17_stop_load.py')

    def test_high_load(self):
        output = run_student_code(self.student_file, [])
        assert "Центральная: 60, Высокая загруженность" in output

    def test_middle_load(self):
        output = run_student_code(self.student_file, [])
        assert "Университет: 50, Средняя загруженность" in output

    def test_low_load(self):
        output = run_student_code(self.student_file, [])
        assert "Заводская: 5, Низкая загруженность" in output
        assert "Парк: -5, Низкая загруженность" in output
