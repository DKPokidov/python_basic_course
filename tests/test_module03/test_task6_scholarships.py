# tests/test_module03/test_task6_scholarships.py
"""
Тесты для задания 6: Стипендии студентов
"""

from tests.test_module03.conftest import run_student_code, get_module03_file


class TestTask6Scholarships:
    """Тесты для задания 6: Стипендии студентов"""

    student_file = get_module03_file('task6_scholarships.py')

    def test_max_scholarship(self):
        output = run_student_code(self.student_file, [])
        assert "Максимальная стипендия: 18000" in output

    def test_min_scholarship(self):
        output = run_student_code(self.student_file, [])
        assert "Минимальная стипендия: 12000" in output

    def test_total(self):
        output = run_student_code(self.student_file, [])
        assert "Общая сумма стипендий: 72000" in output

    def test_unique_values(self):
        output = run_student_code(self.student_file, [])
        assert "12000" in output
        assert "15000" in output
        assert "18000" in output

    def test_sorted_names(self):
        output = run_student_code(self.student_file, [])
        assert "['Анна', 'Иван', 'Мария', 'Ольга', 'Петр']" in output
