# tests/test_module03/test_task12_chessboard_same_color.py
"""
Тесты для задания 12: Шахматная доска — клетки одного цвета
"""

from tests.test_module03.conftest import run_student_code, get_module03_file


class TestTask12ChessboardSameColor:
    """Тесты для задания 12: Шахматная доска — клетки одного цвета"""

    student_file = get_module03_file('task12_chessboard_same_color.py')

    def test_same_color_black(self):
        output = run_student_code(self.student_file, ["1", "1", "2", "2"])
        assert "Клетки одинакового цвета: True" in output

    def test_same_color_white(self):
        output = run_student_code(self.student_file, ["1", "2", "2", "1"])
        assert "Клетки одинакового цвета: True" in output

    def test_different_colors(self):
        output = run_student_code(self.student_file, ["1", "1", "1", "2"])
        assert "Клетки одинакового цвета: False" in output
