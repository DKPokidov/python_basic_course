# tests/test_module05/test_task8_dense_districts.py
"""
Тесты для задания 8: Поиск районов с высокой плотностью населения
"""

from tests.test_module05.conftest import run_student_code, get_module05_file


class TestTask8DenseDistricts:
    """Тесты для задания 8: Поиск районов с высокой плотностью населения"""

    student_file = get_module05_file('task8_dense_districts.py')

    def test_dense_list(self):
        output = run_student_code(self.student_file, [])
        assert "Плотно заселённые районы: ['Центр', 'Старый']" in output
