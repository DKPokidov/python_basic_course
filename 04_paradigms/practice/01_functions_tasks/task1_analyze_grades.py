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
    student_stat = {}
    course_stat = {}
    for student, course, grade in data:
        if student not in student_stat:
            student_stat[student] = [grade, 1]
        else:
            student_stat[student][0] += grade
            student_stat[student][1] += 1
        if course not in course_stat:
            course_stat[course] = [grade, 1]
        else:
            course_stat[course][0] += grade
            course_stat[course][1] += 1
    student_avg = {}
    for student, (grade, grade_number) in student_stat.items():
        student_avg[student] = round(grade / grade_number, 1)
    
    best_course = None
    course_avg = {}
    for course, (grade, grade_quantity) in course_stat.items():
        course_avg[course] = round(grade / grade_quantity, 1)
    best_course = max(course_avg, key=course_avg.get) if course_avg else None 
    return {
        'students_avg': student_avg,
        'best_course': best_course
    }
