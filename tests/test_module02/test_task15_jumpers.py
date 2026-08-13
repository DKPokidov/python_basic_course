# tests/test_module02/test_task15_jumpers.py
"""
Тесты для задания 15: Попрыгунчики
"""

import pytest
from tests.test_module02.conftest import run_student_code, get_module02_file

class TestTask15Jumpers:
    """Тесты для задания 15: Попрыгунчики"""
    
    student_file = get_module02_file('task15_jumpers.py')
    
    def test_jumpers_1_7(self):
        inputs = ["1", "7"]
        output = run_student_code(self.student_file, inputs)
        assert "Расстояние: 6" in output
        assert "да" in output.lower()
    
    def test_jumpers_1_8(self):
        inputs = ["1", "8"]
        output = run_student_code(self.student_file, inputs)
        assert "Расстояние: 7" in output
        assert "нет" in output.lower()
    
    def test_jumpers_10_1(self):
        inputs = ["10", "1"]
        output = run_student_code(self.student_file, inputs)
        assert "Расстояние: 9" in output
        assert "да" in output.lower()
    
    def test_jumpers_10_2(self):
        inputs = ["10", "2"]
        output = run_student_code(self.student_file, inputs)
        assert "Расстояние: 8" in output
        assert "нет" in output.lower()
    
    def test_jumpers_same_house(self):
        inputs = ["5", "5"]
        output = run_student_code(self.student_file, inputs)
        assert "Расстояние: 0" in output
        assert "да" in output.lower()