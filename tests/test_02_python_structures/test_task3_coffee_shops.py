# tests/test_02_python_structures/test_task3_coffee_shops.py
"""
Тесты для задания 3: Рейтинг кофеен
"""

from tests.test_02_python_structures.conftest import run_student_code, get_module03_file


class TestTask3CoffeeShops:
    """Тесты для задания 3: Рейтинг кофеен"""

    student_file = get_module03_file('task3_coffee_shops.py')

    def test_best_shop(self):
        output = run_student_code(self.student_file, [])
        assert "Лучшая кофейня: Цифербург с рейтингом 10" in output
