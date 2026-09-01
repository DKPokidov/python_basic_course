# tests/test_02_python_structures/test_task13_buildings.py
"""
Тесты для задания 13: Анализ списка зданий
"""

from tests.test_02_python_structures.conftest import run_student_code, get_module03_file


class TestTask13Buildings:
    """Тесты для задания 13: Анализ списка зданий"""

    student_file = get_module03_file('task13_buildings.py')

    def test_selected_ids(self):
        output = run_student_code(self.student_file, [])
        assert "[1, 4]" in output
