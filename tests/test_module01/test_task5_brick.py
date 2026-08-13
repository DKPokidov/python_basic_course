# tests/test_module01/test_task5_brick.py

import pytest
from tests.test_module01.conftest import run_student_code, get_module01_file

class TestTask5Brick:
    """Тесты для задания 5: Кирпич"""
    
    student_file = get_module01_file('task5_brick.py')
    
    def test_brick_25_12_6_5(self):
        inputs = ["25", "12", "6.5"]
        output = run_student_code(self.student_file, inputs)
        
        expected_values = {
            "Объём:": "1950.0",
            "Площадь поверхности:": "1081.0",  # <-- ИСПРАВЛЕНО!
            "Сумма рёбер:": "174.0",
            "Масса:": "3.31",
            "Количество кирпичей": "512"
        }
        
        for key, value in expected_values.items():
            assert value in output, f"Ожидалось '{key} {value}', Получено: '{output}'"
    
    def test_brick_10_10_10(self):
        inputs = ["10", "10", "10"]
        output = run_student_code(self.student_file, inputs)
        
        expected_values = {
            "Объём:": "1000.0",
            "Площадь поверхности:": "600.0",
            "Сумма рёбер:": "120.0",
            "Масса:": "1.70",
            "Количество кирпичей": "1000"
        }
        
        for key, value in expected_values.items():
            assert value in output, f"Ожидалось '{key} {value}', Получено: '{output}'"