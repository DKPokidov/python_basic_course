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
    
    for student, course, grade in data:
        if student not in students:
            students[student] = []
        students[student].append(grade)
        
        if course not in courses:
            courses[course] = []
        courses[course].append(grade)
    
    students_avg = {
        student: round(sum(grades) / len(grades), 1) 
        for student, grades in students.items()
    }
    
    best_course = None
    best_avg = -1
    
    for course, grades in courses.items():
        avg_grade = sum(grades) / len(grades)
        if avg_grade > best_avg:
            best_avg = avg_grade
            best_course = course
            
    return {
        "students_avg": students_avg,
        "best_course": best_course
    }
