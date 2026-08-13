# tests/test_module01/test_task8_bench_timer.py
"""
Тесты для задания 8: Умные скамейки
"""

import pytest
from tests.test_module01.conftest import run_student_code, get_module01_file

class TestTask8BenchTimer:
    """Тесты для задания 8: Умные скамейки"""
    
    student_file = get_module01_file('task8_bench_timer.py')
    
    def test_3661(self):
        inputs = ["3661"]
        expected = "1:01:01"
        output = run_student_code(self.student_file, inputs)
        assert expected in output, f"Ожидалось: '{expected}', Получено: '{output}'"
    
    def test_zero(self):
        inputs = ["0"]
        expected = "0:00:00"
        output = run_student_code(self.student_file, inputs)
        assert expected in output, f"Ожидалось: '{expected}', Получено: '{output}'"
    
    def test_86400(self):
        inputs = ["86400"]
        expected = "24:00:00"
        output = run_student_code(self.student_file, inputs)
        assert expected in output, f"Ожидалось: '{expected}', Получено: '{output}'"
    
    def test_61(self):
        inputs = ["61"]
        expected = "0:01:01"
        output = run_student_code(self.student_file, inputs)
        assert expected in output, f"Ожидалось: '{expected}', Получено: '{output}'"