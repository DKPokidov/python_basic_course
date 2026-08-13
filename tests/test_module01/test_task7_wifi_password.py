# tests/test_module01/test_task7_wifi_password.py
"""
Тесты для задания 7: Тайный код от Wi-Fi
"""

import pytest
from tests.test_module01.conftest import run_student_code, get_module01_file

class TestTask7WifiPassword:
    """Тесты для задания 7: Тайный код от Wi-Fi"""
    
    student_file = get_module01_file('task7_wifi_password.py')
    
    def test_789(self):
        inputs = ["789"]
        expected = "7.8.9"
        output = run_student_code(self.student_file, inputs)
        assert expected in output, f"Ожидалось: '{expected}', Получено: '{output}'"
    
    def test_123(self):
        inputs = ["123"]
        expected = "1.2.3"
        output = run_student_code(self.student_file, inputs)
        assert expected in output, f"Ожидалось: '{expected}', Получено: '{output}'"
    
    def test_100(self):
        inputs = ["100"]
        expected = "1.0.0"
        output = run_student_code(self.student_file, inputs)
        assert expected in output, f"Ожидалось: '{expected}', Получено: '{output}'"
    
    def test_999(self):
        inputs = ["999"]
        expected = "9.9.9"
        output = run_student_code(self.student_file, inputs)
        assert expected in output, f"Ожидалось: '{expected}', Получено: '{output}'"