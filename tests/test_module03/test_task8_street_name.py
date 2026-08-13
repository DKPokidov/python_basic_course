# tests/test_module03/test_task8_street_name.py
"""
Тесты для задания 8: Название улицы
"""

from tests.test_module03.conftest import run_student_code, get_module03_file


class TestTask8StreetName:
    """Тесты для задания 8: Название улицы"""

    student_file = get_module03_file('task8_street_name.py')

    def test_short_name(self):
        output = run_student_code(self.student_file, ["Луначарского"])
        assert "True" in output

    def test_empty_name(self):
        output = run_student_code(self.student_file, [""])
        assert "False" in output

    def test_too_long_name(self):
        output = run_student_code(
            self.student_file,
            ["Улица с очень длинным названием, превышающим тридцать символов"],
        )
        assert "False" in output
