# tests/test_module08/test_task5_university.py
"""
Тесты для задания 5: Университет
"""

import importlib.util
from tests.test_module08.conftest import get_module08_file


def load_student_code(student_file):
    spec = importlib.util.spec_from_file_location("student_module", student_file)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class TestTask5University:
    """Тесты для задания 5: Университет"""

    student_file = get_module08_file('task5_university.py')

    def test_create_student(self):
        mod = load_student_code(self.student_file)
        s = mod.Student("Алиса", "345", 4.5)
        assert s.name == "Алиса"
        assert s.group == "345"
        assert s.average_grade == 4.5

    def test_improve_grade(self):
        mod = load_student_code(self.student_file)
        s = mod.Student("Алиса", "345", 4.0)
        s.improve_grade(0.7)
        assert s.average_grade == 4.7

    def test_improve_grade_cap(self):
        mod = load_student_code(self.student_file)
        s = mod.Student("Алиса", "345", 4.8)
        s.improve_grade(0.5)
        assert s.average_grade == 5.0

    def test_initial_grade_cap(self):
        mod = load_student_code(self.student_file)
        s = mod.Student("Борис", "345", 5.5)
        assert s.average_grade == 5.0

    def test_create_university(self):
        mod = load_student_code(self.student_file)
        u = mod.University("ITMO")
        assert u.name == "ITMO"
        assert u.students == []

    def test_enroll_student(self):
        mod = load_student_code(self.student_file)
        u = mod.University("ITMO")
        s = mod.Student("Алиса", "345", 4.5)
        u.enroll_student(s)
        assert len(u.students) == 1

    def test_get_top_students(self):
        mod = load_student_code(self.student_file)
        u = mod.University("ITMO")
        s1 = mod.Student("Алиса", "345", 4.5)
        s2 = mod.Student("Борис", "345", 4.8)
        s3 = mod.Student("Вика", "346", 3.9)
        u.enroll_student(s1)
        u.enroll_student(s2)
        u.enroll_student(s3)
        top = u.get_top_students(2)
        assert len(top) == 2
        assert top[0].name == "Борис"
        assert top[1].name == "Алиса"

    def test_get_students_by_group(self):
        mod = load_student_code(self.student_file)
        u = mod.University("ITMO")
        s1 = mod.Student("Алиса", "345", 4.5)
        s2 = mod.Student("Борис", "345", 4.8)
        s3 = mod.Student("Вика", "346", 3.9)
        u.enroll_student(s1)
        u.enroll_student(s2)
        u.enroll_student(s3)
        group_345 = u.get_students_by_group("345")
        assert len(group_345) == 2
        assert group_345[0].name == "Алиса"
        assert group_345[1].name == "Борис"

    def test_get_students_by_group_empty(self):
        mod = load_student_code(self.student_file)
        u = mod.University("ITMO")
        s1 = mod.Student("Алиса", "345", 4.5)
        u.enroll_student(s1)
        result = u.get_students_by_group("999")
        assert result == []

    def test_repr(self):
        mod = load_student_code(self.student_file)
        s = mod.Student("Алиса", "345", 4.5)
        r = repr(s)
        assert "Алиса" in r
        assert "345" in r
        assert "4.5" in r
