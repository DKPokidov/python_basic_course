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
    disciplines = {}
    for student in data:
        name, discipline, grade = student
        if name not in students:
            students[name] = grade
        else:
            students[name] = (students[name] + grade) / 2
        if discipline not in disciplines:
            disciplines[discipline] = grade
        else:
            disciplines[discipline] = (disciplines[discipline] + grade) / 2
    best_course = None
    best_grade = 0
    for discipline in disciplines.items():
        if discipline[1] > best_grade:
            best_course = discipline[0]
            best_grade = discipline[1]
    result = {
        'students_avg': students,
        'best_course': best_course
        }
    return(result)
