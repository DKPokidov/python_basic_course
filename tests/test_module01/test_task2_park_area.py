# tests/test_module01/test_task2_park_area.py
"""
Тесты для задания 2: Помощь чиновнику
"""

import pytest
from tests.test_module01.conftest import run_student_code, get_module01_file

class TestTask2ParkArea:
    """Тесты для задания 2: Помощь чиновнику"""
    
    student_file = get_module01_file('task2_park_area.py')
    
    def test_area_10_5(self):
        inputs = ["10", "5"]
        expected = "50.0"
        output = run_student_code(self.student_file, inputs)
        assert expected in output, f"Ожидалось: '{expected}', Получено: '{output}'"
    
    def test_area_7_5_3_2(self):
        inputs = ["7.5", "3.2"]
        expected = "24.0"
        output = run_student_code(self.student_file, inputs)
        assert expected in output, f"Ожидалось: '{expected}', Получено: '{output}'"
    
    def test_area_zero(self):
        inputs = ["0", "5"]
        expected = "0.0"
        output = run_student_code(self.student_file, inputs)
        assert expected in output, f"Ожидалось: '{expected}', Получено: '{output}'"