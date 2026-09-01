# tests/test_01_python_basics/test_task14_formula.py
"""
Тесты для задания 14: Злая формула
"""

import pytest
from tests.test_01_python_basics.conftest import run_student_code, get_module02_file

class TestTask14Formula:
    """Тесты для задания 14: Злая формула"""
    
    student_file = get_module02_file('task14_formula.py')
    
    def test_formula_5_3(self):
        inputs = ["5", "3"]
        output = run_student_code(self.student_file, inputs)
        assert "2.008" in output, f"Ожидалось: '2.008', Получено: '{output}'"
    
    def test_formula_10_2(self):
        inputs = ["10", "2"]
        output = run_student_code(self.student_file, inputs)
        assert "2.066" in output, f"Ожидалось: '2.066', Получено: '{output}'"
    
    def test_formula_3_7(self):
        inputs = ["3", "7"]
        output = run_student_code(self.student_file, inputs)
        assert "1.909" in output, f"Ожидалось: '1.909', Получено: '{output}'"