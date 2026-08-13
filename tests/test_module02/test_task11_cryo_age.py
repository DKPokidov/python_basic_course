# tests/test_module02/test_task11_cryo_age.py
"""
Тесты для задания 11: Криокапсула будущего
"""

import pytest
from tests.test_module02.conftest import run_student_code, get_module02_file

class TestTask11CryoAge:
    """Тесты для задания 11: Криокапсула будущего"""
    
    student_file = get_module02_file('task11_cryo_age.py')
    
    def test_cryo_age_2000(self):
        inputs = ["2000"]
        expected = "184 лет"
        output = run_student_code(self.student_file, inputs)
        assert expected in output, f"Ожидалось: '{expected}', Получено: '{output}'"
    
    def test_cryo_age_2024(self):
        inputs = ["2024"]
        expected = "160 лет"
        output = run_student_code(self.student_file, inputs)
        assert expected in output, f"Ожидалось: '{expected}', Получено: '{output}'"
    
    def test_cryo_age_2184(self):
        inputs = ["2184"]
        expected = "0 лет"
        output = run_student_code(self.student_file, inputs)
        assert expected in output, f"Ожидалось: '{expected}', Получено: '{output}'"