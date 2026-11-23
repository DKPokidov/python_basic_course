"""
Задание 5: Университет

В деканате завели электронный журнал успеваемости. Нужна модель студента
(имя, группа, средний балл) и модель университета — чтобы зачислять
студентов, формировать списки лучших для стипендии и находить студентов
по группам для объявлений.

Создайте класс Student:
- атрибуты: name, group, average_grade;
- в __init__ начальная оценка не должна превышать 5.0 (если передано
  больше — ограничьте до 5.0);
- метод improve_grade(points) увеличивает average_grade на points,
  но не более 5.0;
- метод __repr__ возвращает строку, содержащую имя, группу и оценку.

Создайте класс University:
- атрибуты: name и students (список, по умолчанию пустой);
- enroll_student(student) — добавляет студента;
- get_top_students(n) — возвращает n лучших студентов
  (по average_grade, по убыванию);
- get_students_by_group(group_name) — возвращает список студентов
  указанной группы в порядке зачисления.
"""


class Student:
    def __init__(self, name, group, average_grade):
        self.name = name
        self.group = group
        self.average_grade = min(float(average_grade), 5.0)

    def improve_grade(self, points):
        self.average_grade = min(float(self.average_grade + points), 5.0)
        return self.average_grade

    def __repr__(self):
        return f'Имя: {self.name}, группа: {self.group}, оценка: {self.average_grade}.'


class University:
    def __init__(self, name, students=None):
        self.name = name
        self.students = list(students) if students is not None else []

    def enroll_student(self, student):
        self.students.append(student)

    def get_top_students(self, n):
        if n <= 0:
            return []
        sorted_list = sorted(self.students, key=lambda student: student.average_grade, reverse=True)
        return sorted_list[:n]

    def get_students_by_group(self, group_name):
        group_list = []
        for student in self.students:
            if student.group == group_name:
                group_list.append(student)
        return group_list