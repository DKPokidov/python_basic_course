"""
Задание 1: Анализ успеваемости студентов

Функция analyze_grades(data) анализирует успеваемость студентов.

Вход: список кортежей (имя, курс, оценка)
Вывод (print): ничего (функция возвращает результат)
Возвращает словарь: {'students_avg': {имя: средний_балл}, 'best_course': название_курса}
Требования: один проход, округление до 1 знака
"""


def analyze_grades(data):
    students = {}
    courses = {}
    for name, course, grade in data:
        if name not in students:
            students[name] = [0, 0]
        students[name][0] += grade
        students[name][1] += 1
        if course not in courses:
            courses[course] = [0, 0]
        courses[course][0] += grade
        courses[course][1] += 1

    students_avg = {name: round(sum[0] / sum[1], 1) for name, sum in students.items()}
    best_course = max(courses, key=lambda c: courses[c][0] / courses[c][1])
    return {'students_avg': students_avg, 'best': best_course}