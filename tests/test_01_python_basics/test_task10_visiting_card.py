# tests/test_01_python_basics/test_task10_visiting_card.py
"""
Тесты для задания 10: Простая визитка
"""

import pytest
from tests.test_01_python_basics.conftest import run_student_code, get_module02_file

class TestTask10VisitingCard:
    """Тесты для задания 10: Простая визитка"""
    
    student_file = get_module02_file('task10_visiting_card.py')
    
    def test_visiting_card_1(self):
        inputs = ["Венчурный инвестор", "Иван", "Петров"]
        expected = "Пользователь: Венчурный инвестор Иван Петров"
        output = run_student_code(self.student_file, inputs)
        assert expected in output, f"Ожидалось: '{expected}', Получено: '{output}'"
    
    def test_visiting_card_2(self):
        inputs = ["Криптоблогер", "Анна", "Сидорова"]
        expected = "Пользователь: Криптоблогер Анна Сидорова"
        output = run_student_code(self.student_file, inputs)
        assert expected in output, f"Ожидалось: '{expected}', Получено: '{output}'"