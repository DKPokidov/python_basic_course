"""
Задание 1: Анализ успеваемости студентов

Функция analyze_grades(data) анализирует успеваемость студентов.

Вход: список кортежей (имя, курс, оценка)
Вывод (print): ничего (функция возвращает результат)
Возвращает словарь: {'students_avg': {имя: средний_балл}, 'best_course': название_курса}
Требования: один проход, округление до 1 знака
"""

# НАПИШИТЕ ВАШ КОД ЗДЕСЬ
# 04_paradigms/practice/01_functions_tasks/task1_analyze_grades.py


def analyze_grades(data):
    student_grades = {}
    course_grades = {}
    for name, course, grade in data:
        if name not in student_grades:
            student_grades[name] = []
        student_grades[name].append(grade)
        if course not in course_grades:
            course_grades[course] = []
        course_grades[course].append(grade)
    students_avg = {}
    for name, grades in student_grades.items():
        students_avg[name] = round(sum(grades) / len(grades), 1)
    best_course = None
    best_avg = 0
    for course, grades in course_grades.items():
        avg = sum(grades) / len(grades)
        if avg > best_avg:
            best_avg = avg
            best_course = course
    return {'students_avg': students_avg, 'best_course': best_course}
