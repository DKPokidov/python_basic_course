# tests/test_01_python_basics/test_task1_survey.py
"""
Тесты для задания 1: Анкета для соцопроса
"""

import pytest
from tests.test_01_python_basics.conftest import run_student_code, get_module01_file

class TestTask1Survey:
    """Тесты для задания 1: Анкета для соцопроса"""
    
    student_file = get_module01_file('task1_survey.py')
    
    def test_hello_ivan(self):
        inputs = ["Иван", "20"]
        expected = "Привет, Иван! Тебе 20 лет."
        output = run_student_code(self.student_file, inputs)
        assert expected in output, f"Ожидалось: '{expected}', Получено: '{output}'"
    
    def test_hello_maria(self):
        inputs = ["Мария", "18"]
        expected = "Привет, Мария! Тебе 18 лет."
        output = run_student_code(self.student_file, inputs)
        assert expected in output, f"Ожидалось: '{expected}', Получено: '{output}'"
    
    def test_hello_alexey(self):
        inputs = ["Алексей", "0"]
        expected = "Привет, Алексей! Тебе 0 лет."
        output = run_student_code(self.student_file, inputs)
        assert expected in output, f"Ожидалось: '{expected}', Получено: '{output}'"
    
    def test_hello_anna(self):
        inputs = ["Анна", "100"]
        expected = "Привет, Анна! Тебе 100 лет."
        output = run_student_code(self.student_file, inputs)
        assert expected in output, f"Ожидалось: '{expected}', Получено: '{output}'"
    
    def test_hello_with_spaces(self):
        inputs = ["Анна Мария", "25"]
        expected = "Привет, Анна Мария! Тебе 25 лет."
        output = run_student_code(self.student_file, inputs)
        assert expected in output, f"Ожидалось: '{expected}', Получено: '{output}'"