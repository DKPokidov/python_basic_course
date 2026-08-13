# tests/test_module01/test_task9_time_diff.py
"""
Тесты для задания 9: Счастливых часов не наблюдают
"""

import pytest
from tests.test_module01.conftest import run_student_code, get_module01_file

class TestTask9TimeDiff:
    """Тесты для задания 9: Счастливых часов не наблюдают"""
    
    student_file = get_module01_file('task9_time_diff.py')
    
    def test_9_to_12_30(self):
        inputs = ["9", "0", "0", "12", "30", "0"]
        expected = "3:30:00"
        output = run_student_code(self.student_file, inputs)
        assert expected in output, f"Ожидалось: '{expected}', Получено: '{output}'"
    
    def test_23_to_1(self):
        inputs = ["23", "0", "0", "1", "0", "0"]
        expected = "2:00:00"
        output = run_student_code(self.student_file, inputs)
        assert expected in output, f"Ожидалось: '{expected}', Получено: '{output}'"
    
    def test_same_time(self):
        inputs = ["12", "0", "0", "12", "0", "0"]
        expected = "0:00:00"
        output = run_student_code(self.student_file, inputs)
        assert expected in output, f"Ожидалось: '{expected}', Получено: '{output}'"
    
    def test_8_30_to_17_45(self):
        inputs = ["8", "30", "0", "17", "45", "0"]
        expected = "9:15:00"
        output = run_student_code(self.student_file, inputs)
        assert expected in output, f"Ожидалось: '{expected}', Получено: '{output}'"