# tests/test_01_python_basics/test_task3_coins.py
"""
Тесты для задания 3: Счет мелких денег
"""

import pytest
from tests.test_01_python_basics.conftest import run_student_code, get_module01_file

class TestTask3Coins:
    """Тесты для задания 3: Счет мелких денег"""
    
    student_file = get_module01_file('task3_coins.py')
    
    def test_coins_1_2_3_4(self):
        inputs = ["1", "2", "3", "4"]
        expected = "0 руб. 89 коп."
        output = run_student_code(self.student_file, inputs)
        assert expected in output, f"Ожидалось: '{expected}', Получено: '{output}'"
    
    def test_coins_2_0_0_0(self):
        inputs = ["2", "0", "0", "0"]
        expected = "1 руб. 0 коп."
        output = run_student_code(self.student_file, inputs)
        assert expected in output, f"Ожидалось: '{expected}', Получено: '{output}'"
    
    def test_coins_zero(self):
        inputs = ["0", "0", "0", "0"]
        expected = "0 руб. 0 коп."
        output = run_student_code(self.student_file, inputs)
        assert expected in output, f"Ожидалось: '{expected}', Получено: '{output}'"
    
    def test_coins_10_10_10_10(self):
        inputs = ["10", "10", "10", "10"]
        expected = "6 руб. 60 коп."
        output = run_student_code(self.student_file, inputs)
        assert expected in output, f"Ожидалось: '{expected}', Получено: '{output}'"