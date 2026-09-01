# tests/test_02_python_structures/test_task10_pirate_ship.py
"""
Тесты для задания 10: Пиратские корабли
"""

from tests.test_02_python_structures.conftest import run_student_code, get_module03_file


class TestTask10PirateShip:
    """Тесты для задания 10: Пиратские корабли"""

    student_file = get_module03_file('task10_pirate_ship.py')

    def test_black_with_skull(self):
        output = run_student_code(self.student_file, ["черный", "череп"])
        assert "Осторожно пираты!" in output

    def test_black_empty_drawing(self):
        output = run_student_code(self.student_file, ["черный", ""])
        assert "Осторожно пираты!" in output

    def test_white_flag_with_skull(self):
        output = run_student_code(self.student_file, ["белый", "череп"])
        assert "Корабль не опасен!" in output

    def test_black_striped_flag(self):
        output = run_student_code(self.student_file, ["черный", "полосатый"])
        assert "Корабль не опасен!" in output
