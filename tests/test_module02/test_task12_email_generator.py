# tests/test_module02/test_task12_email_generator.py
"""
Тесты для задания 12: Генератор email-адреса
"""

import pytest
from tests.test_module02.conftest import run_student_code, get_module02_file

class TestTask12EmailGenerator:
    """Тесты для задания 12: Генератор email-адреса"""
    
    student_file = get_module02_file('task12_email_generator.py')
    
    def test_email_alexey_2026(self):
        inputs = ["Алексей", "2026"]
        expected = "Алексей2026@itmo.com"
        output = run_student_code(self.student_file, inputs)
        assert expected in output, f"Ожидалось: '{expected}', Получено: '{output}'"
    
    def test_email_maria_2025(self):
        inputs = ["Мария", "2025"]
        expected = "Мария2025@itmo.com"
        output = run_student_code(self.student_file, inputs)
        assert expected in output, f"Ожидалось: '{expected}', Получено: '{output}'"