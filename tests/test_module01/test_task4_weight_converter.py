# tests/test_module01/test_task4_weight_converter.py
"""
Тесты для задания 4: Международный весооборот
"""

import pytest
from tests.test_module01.conftest import run_student_code, get_module01_file

class TestTask4WeightConverter:
    """Тесты для задания 4: Международный весооборот"""
    
    student_file = get_module01_file('task4_weight_converter.py')
    
    def test_10_kg(self):
        inputs = ["10 кг"]
        expected = "10.0 кг = 10.000000 кг"
        output = run_student_code(self.student_file, inputs)
        assert expected in output, f"Ожидалось: '{expected}', Получено: '{output}'"
    
    def test_1_t(self):
        inputs = ["1 т"]
        expected = "1.0 т = 1000.000000 кг"
        output = run_student_code(self.student_file, inputs)
        assert expected in output, f"Ожидалось: '{expected}', Получено: '{output}'"
    
    def test_1_pud(self):
        inputs = ["1 пуд"]
        expected = "1.0 пуд = 16.000000 кг"
        output = run_student_code(self.student_file, inputs)
        assert expected in output, f"Ожидалось: '{expected}', Получено: '{output}'"
    
    def test_100_g(self):
        inputs = ["100 г"]
        expected = "100.0 г = 0.100000 кг"
        output = run_student_code(self.student_file, inputs)
        assert expected in output, f"Ожидалось: '{expected}', Получено: '{output}'"