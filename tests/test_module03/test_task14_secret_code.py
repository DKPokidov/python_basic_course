# tests/test_module03/test_task14_secret_code.py
"""
Тесты для задания 14: Секретный код доступа
"""

from tests.test_module03.conftest import run_student_code, get_module03_file


class TestTask14SecretCode:
    """Тесты для задания 14: Секретный код доступа"""

    student_file = get_module03_file('task14_secret_code.py')

    def test_valid_code(self):
        output = run_student_code(self.student_file, ["Ab1#xyz7"])
        assert "True" in output

    def test_no_uppercase(self):
        output = run_student_code(self.student_file, ["abcdefgh"])
        assert "False" in output

    def test_no_lowercase(self):
        output = run_student_code(self.student_file, ["ABCDEFGH"])
        assert "False" in output

    def test_no_digit(self):
        output = run_student_code(self.student_file, ["Abcdefgh"])
        assert "False" in output

    def test_special_at_start(self):
        output = run_student_code(self.student_file, ["#Ab1x7yz"])
        assert "False" in output

    def test_two_specials(self):
        output = run_student_code(self.student_file, ["A1#@bcde"])
        assert "False" in output

    def test_wrong_length(self):
        output = run_student_code(self.student_file, ["Ab1#x7y"])
        assert "False" in output
