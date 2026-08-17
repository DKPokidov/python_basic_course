# tests/test_module06/test_task1_analyze_grades.py
"""
Тесты для задания 1: Анализ успеваемости студентов
"""

import importlib.util
from tests.test_module06.conftest import get_module06_file


def load_student_code(student_file):
    spec = importlib.util.spec_from_file_location("student_module", student_file)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class TestTask1AnalyzeGrades:
    """Тесты для задания 1: Анализ успеваемости студентов"""

    student_file = get_module06_file('task1_analyze_grades.py')

    def test_basic(self):
        mod = load_student_code(self.student_file)
        data = [("Алиса", "Математика", 5), ("Борис", "Математика", 4), ("Алиса", "Физика", 4), ("Борис", "Физика", 5)]
        result = mod.analyze_grades(data)
        assert result['students_avg']['Алиса'] == 4.5
        assert result['students_avg']['Борис'] == 4.5
        assert result['best_course'] == 'Математика'

    def test_one_student(self):
        mod = load_student_code(self.student_file)
        data = [("Алиса", "История", 5)]
        result = mod.analyze_grades(data)
        assert result['students_avg']['Алиса'] == 5.0
        assert result['best_course'] == 'История'

    def test_different_grades(self):
        mod = load_student_code(self.student_file)
        data = [("Алиса", "Химия", 5), ("Алиса", "Химия", 3), ("Борис", "Биология", 4)]
        result = mod.analyze_grades(data)
        assert result['students_avg']['Алиса'] == 4.0
        assert result['students_avg']['Борис'] == 4.0
        assert result['best_course'] == 'Химия'

    def test_rounding(self):
        mod = load_student_code(self.student_file)
        data = [("Алиса", "Литература", 5), ("Борис", "Литература", 4), ("Вика", "Литература", 3)]
        result = mod.analyze_grades(data)
        assert result['students_avg']['Алиса'] == 5.0
        assert result['students_avg']['Борис'] == 4.0
        assert result['students_avg']['Вика'] == 3.0
