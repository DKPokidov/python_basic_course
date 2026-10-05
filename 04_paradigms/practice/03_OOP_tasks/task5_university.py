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
    name = ""
    group = ""
    average_grade = 0

    def __init__(self, name, group, average_grade):
        self.name = name
        self.group = group
        self.average_grade = min(average_grade, 5.0)

    def improve_grade(self, points):
        self.average_grade = min(self.average_grade + points, 5.0)

    def __repr__(self):
        return f"{self.name}, группа {self.group}, средняя оценка - {self.average_grade}"


class University:
    name = ""
    students = []

    def __init__(self, name):
        self.name = name

    def enroll_student(self, student):
        self.students.append(student)

    def get_top_students(self, n):
        studentList = sorted(self.students, key=lambda s: s.average_grade, reverse=True)

        return studentList[:n]

    def get_students_by_group(self, group_name):
        studentList = []
        for student in self.students:
            if student.group == group_name:
                studentList.append(student)

        return studentList
