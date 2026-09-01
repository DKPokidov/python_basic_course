# tests/test_01_python_basics/test_task13_story_maker.py
"""
Тесты для задания 13: Сочинитель сказок
"""

import pytest
from tests.test_01_python_basics.conftest import run_student_code, get_module02_file

class TestTask13StoryMaker:
    """Тесты для задания 13: Сочинитель сказок"""
    
    student_file = get_module02_file('task13_story_maker.py')
    
    def test_story_default(self):
        inputs = [
            "Дедди", "котлеты", "ученым", "делать опыты",
            "Воронеж", "Ворон", "Привет, дружище!", "Привет!", "ученым"
        ]
        output = run_student_code(self.student_file, inputs)
        
        expected_parts = [
            "Жил-был хомяк по имени Дедди",
            "Дедди очень любил есть котлеты",
            "мечтал стать ученым",
            "научился делать опыты",
            "отправился в Воронеж",
            "встретил Ворон",
            "Привет, дружище!",
            "Привет!",
            "самым ученым хомяком"
        ]
        
        for part in expected_parts:
            assert part in output, f"Ожидалось: '{part}', Получено: '{output}'"