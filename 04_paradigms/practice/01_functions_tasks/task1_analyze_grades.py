"""
Задание 1: Анализ успеваемости студентов

Вы — аналитик в деканате. После сессии у вас стопка журналов: по каждому
студенту и каждой дисциплине есть запись с оценкой. Один и тот же студент
встречается несколько раз — по разу на дисциплину. Деканат хочет знать
два числа: средний балл каждого студента и курс, который сдавался
лучше всех.

Напишите функцию analyze_grades(data), где data — список кортежей
(имя студента, курс, оценка). Функция за один проход:

1) считает средний балл каждого студента (сумма оценок / число оценок),
   округлённый до 1 знака;
2) находит курс с наибольшим средним баллом среди всех своих студентов.
   Если у нескольких курсов средние баллы совпали, берётся курс, первым
   встретившийся в данных.

Функция ничего не печатает и возвращает словарь:
    {'students_avg': {имя: средний_балл}, 'best_course': название_курса}
"""


def analyze_grades(data):
    students_grades = {}
    course_grades = {}
    students_avg = {}
    course_avg = {}

    for name, course, grade in data:
        if name not in students_grades:
            students_grades[name] = []

        students_grades[name].append(grade)

        if course not in course_grades:
            course_grades[course] = []

        course_grades[course].append(grade)

    for name, grades in students_grades.items():
        students_avg[name] = round(sum(grades) / len(grades), 1)

    for course, grades in course_grades.items():
        course_avg[course] = sum(grades) / len(grades)

    best_course = max(course_avg, key=course_avg.get)

    return {'students_avg': students_avg, 'best_course': best_course}