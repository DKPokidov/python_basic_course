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
    all_courses = {}
    all_students = {}
    for elem in data:
        if elem[0] in all_students:
            all_students[elem[0]][0] += elem[2]
            all_students[elem[0]][1] += 1
        else:
            all_students.update({elem[0]: [elem[2], 1]})
        if elem[1] in all_courses:
            all_courses[elem[1]][0] += elem[2]
            all_courses[elem[1]][1] += 1
        else:
            all_courses.update({elem[1]: [elem[2], 1]})
    for person, grades in all_students.items():
        average = round(grades[0] / grades[1], 1)
        all_students[person] = average
    for course, meaning in all_courses.items():
        average_course = round(meaning[0] / meaning[1], 1)
        all_courses[course] = average_course
    max_score = max(all_courses.values())
    for course, meaning in all_courses.items():
        if meaning == max_score:
            best_course = course
            break
    return {"students_avg": all_students, "best_course": best_course}
