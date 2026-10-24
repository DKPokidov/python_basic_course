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
        if average_grade > 5:
            self.average_grade = 5.0
        else:
            self.average_grade = average_grade

    def improve_grade(self, points):
        new_grade = self.average_grade + points
        if new_grade > 5:
            self.average_grade = 5.0
        else:
            self.average_grade = new_grade


class University:
    def __init__(self, name):
        self.name = name
        self.students = []

    def enroll_student(self, student):
        self.students.append(student)

    def get_top_students(self, n):
        top_students = self.students.copy()
        n = len(top_students)
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if top_students[j] > top_students[j + 1]:
                    top_students[j], top_students[j + 1] = top_students[j + 1], top_students[j]
        top_students.reverse()
        return top_students[:n]

    def get_students_by_group(self, group_name):
        return [student for student in self.students if student.group == group_name]
