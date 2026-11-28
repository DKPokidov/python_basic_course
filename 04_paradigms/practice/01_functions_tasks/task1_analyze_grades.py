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
    all_students = []
    courses = []
    for tuple_ in data:
        if tuple_[0] not in all_students:
            all_students.append(tuple_[0])
        if tuple_[1] not in courses:
            courses.append(tuple_[1])
    grade_summary = [0 for i in range(len(courses))]
    grade_counter = [0 for i in range(len(courses))]
    for tuple_ in data:
        grade_summary[courses.index(tuple_[1])] += tuple_[2]
        grade_counter[courses.index(tuple_[1])] += 1
    grade_avg = []
    for i in range(len(grade_summary)):
        grade_avg.append(round((grade_summary[i] / grade_counter[i]), 1))
    best_course = courses[grade_avg.index(max(grade_avg))]
    student_grades = [0 for i in range(len(all_students))]
    student_grades_counter = [0 for i in range(len(all_students))]
    student_grade_avg = []
    for tuple_ in data:
            student_grades[all_students.index(tuple_[0])] += tuple_[2]
            student_grades_counter[all_students.index(tuple_[0])] += 1
    for i in range(len(student_grades)):
            student_grade_avg.append(round((student_grades[i] / student_grades_counter[i]), 1))
    dict_student = {}
    for i in range(len(all_students)):
         dict_student[all_students[i]] = student_grade_avg[i]
    return {'students_avg': dict_student, 'best_course': best_course}