# tests/test_module01/test_task6_call_duration.py
"""
Тесты для задания 6: Миша и его деньги
"""

import pytest
from tests.test_module01.conftest import run_student_code, get_module01_file

class TestTask6CallDuration:
    """Тесты для задания 6: Миша и его деньги"""
    
    student_file = get_module01_file('task6_call_duration.py')
    
    def test_53_to_8(self):
        inputs = ["53", "8"]
        expected = "18 минут"
        output = run_student_code(self.student_file, inputs)
        assert expected in output, f"Ожидалось: '{expected}', Получено: '{output}'"
    
    def test_100_to_75(self):
        inputs = ["100", "75"]
        expected = "10 минут"
        output = run_student_code(self.student_file, inputs)
        assert expected in output, f"Ожидалось: '{expected}', Получено: '{output}'"
    
    def test_100_to_97_5(self):
        inputs = ["100", "97.5"]
        expected = "1 минут"
        output = run_student_code(self.student_file, inputs)
        assert expected in output, f"Ожидалось: '{expected}', Получено: '{output}'"
    
    def test_50_to_0(self):
        inputs = ["50", "0"]
        expected = "20 минут"
        output = run_student_code(self.student_file, inputs)
        assert expected in output, f"Ожидалось: '{expected}', Получено: '{output}'"