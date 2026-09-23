"""
Задание 5: Университет

Создайте класс Student:
- атрибуты: name, group, average_grade;
- в __init__ начальная оценка не должна превышать 5.0 (если передано больше — ограничьте до 5.0);
- метод improve_grade(points) увеличивает average_grade на points, но не более 5.0;
- метод __repr__ возвращает строку, содержащую имя, группу и оценку.

Создайте класс University:
- атрибуты: name и students (список, по умолчанию пустой);
- enroll_student(student) — добавляет студента;
- get_top_students(n) — возвращает n лучших студентов (по average_grade, по убыванию);
- get_students_by_group(group_name) — возвращает список студентов указанной группы
  (в порядке зачисления).
"""


class Student:
    def __init__(self, name, group, average_grade):
        pass

    def improve_grade(self, points):
        pass


class University:
    def __init__(self, name):
        pass

    def enroll_student(self, student):
        pass

    def get_top_students(self, n):
        pass

    def get_students_by_group(self, group_name):
        pass