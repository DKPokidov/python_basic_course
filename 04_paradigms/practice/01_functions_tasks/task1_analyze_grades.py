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
    sum_student = {}
    count_student ={}
    sum_course = {}
    count_course = {}
    for name, course, grade in data:
        sum_student[name] = sum_student.get(name, 0) + grade
        count_student[name] = count_student.get(name, 0) + 1
        sum_course[course] = sum_course.get(course, 0) + grade
        count_course[course] = count_course.get(course, 0) + 1
    srednee_student = {}
    for name in sum_student:
        srednee_student[name] = round(sum_student[name] / count_student[name], 1)
    best_course = 0
    srednee_best= 0
    for course in sum_course:
         srednee_course = sum_course[course] / count_course[course]

         if srednee_best == 0 and srednee_course > srednee_best:
             srednee_best = srednee_course
             best_course = course
    return {'students_avg': srednee_student, 'best_course': best_course}



    