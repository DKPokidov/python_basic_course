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
    students = {}
    courses = {}
    courses_avg = {}
    result = {'students_avg': {}, 'best_course': ''}
    for row in data:
        name = row[0]
        course = row[1]
        grade = row[2]
        if students.get(name) is None:
            students[name] = [grade]
        else:
            students[name].append(grade)
        if courses.get(course) is None:
            courses[course] = [grade]
        else:
            courses[course].append(grade)
    for student, grades in students:
        result['students_avg'][student] = round(sum(grades) / len(grades), 1)
    for course, grades in courses:
        courses_avg[course] = round(sum(grades) / len(grades), 1)
    for course, aver in courses_avg:
        if aver == max(courses.values()):
            result['best_course'] = course
            break
    return result
