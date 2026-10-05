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
    studentGrades = {}
    courseGrades = {}

    for i in data:
        if studentGrades.get(i[0]) is not None:
            studentGrades[i[0]].append(i[2])
        else:
            studentGrades[i[0]] = [i[2]]
        
        if courseGrades.get(i[1]) is not None:
            courseGrades[i[1]].append(i[2])
        else:
            courseGrades[i[1]] = [i[2]]

    averageStudentGrades = {key: sum(values) / len(values) for key, values in studentGrades.items()}
    averageCourseGrades = {key: sum(values) / len(values) for key, values in courseGrades.items()}

    return {"students_avg": averageStudentGrades, "best_course": max(averageCourseGrades, key=averageCourseGrades.get)}

# inputData = [("Ivan", "ds", 2), ("Ivan", "da", 5), ("Sasha", "ds", 1)]

# print(analyze_grades(inputData))
