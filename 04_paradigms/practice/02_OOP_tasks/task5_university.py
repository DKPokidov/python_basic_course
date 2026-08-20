"""
Задание 5: Университет

Создайте класс Student с атрибутами: name, group, average_grade.
Метод improve_grade(points) увеличивает average_grade на points, но не более 5.0.
Создайте класс University с атрибутом name и списком students.
Методы:
- enroll_student(student) — добавляет студента
- get_top_students(n) — возвращает n лучших студентов (по average_grade, по убыванию)
- get_students_by_group(group_name) — возвращает список студентов указанной группы
"""

# НАПИШИТЕ ВАШ КОД ЗДЕСЬ
# 04_paradigms/practice/03_OOP_tasks/task5_university.py


class Student:
    def __init__(self, name, group, average_grade):
        self.name = name
        self.group = group
        self.average_grade = min(average_grade, 5.0)

    def improve_grade(self, points):
        self.average_grade = min(self.average_grade + points, 5.0)

    def __repr__(self):
        return f"Студент {self.name}, группа {self.group}, средний балл {self.average_grade}"


class University:
    def __init__(self, name=""):
        self.name = name
        self.students = []

    def enroll_student(self, student):
        self.students.append(student)

    def get_top_students(self, n):
        return sorted(self.students, key=lambda s: s.average_grade, reverse=True)[:n]

    def get_students_by_group(self, group_name):
        return [s for s in self.students if s.group == group_name]
