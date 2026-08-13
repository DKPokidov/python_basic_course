# tests/test_module03/test_task11_chessboard_white.py
"""
Тесты для задания 11: Шахматная доска — проверка белого поля
"""

from tests.test_module03.conftest import run_student_code, get_module03_file


class TestTask11ChessboardWhite:
    """Тесты для задания 11: Шахматная доска — проверка белого поля"""

    student_file = get_module03_file('task11_chessboard_white.py')

    def test_black_field(self):
        output = run_student_code(self.student_file, ["1", "1"])
        assert "Поле белое: False" in output

    def test_white_field(self):
        output = run_student_code(self.student_file, ["1", "2"])
        assert "Поле белое: True" in output

    def test_white_field_corner(self):
        output = run_student_code(self.student_file, ["8", "1"])
        assert "Поле белое: True" in output

    def test_black_field_even(self):
        output = run_student_code(self.student_file, ["2", "2"])
        assert "Поле белое: False" in output
