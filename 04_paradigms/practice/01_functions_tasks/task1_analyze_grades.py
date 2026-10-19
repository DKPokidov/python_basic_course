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
    dict_students = {}
    dict_subjects = {}
    for cur in data:
        name, subject, grade = cur
        try:
            dict_students[name].append(grade)
        except:
            dict_students[name] = [grade]
        try:
            dict_subjects[subject].append(grade)
        except:
            dict_subjects[subject] = [grade]
    dict_final = {"students_avg": {}, "best_course": ""}
    for i in dict_students:
        cur = dict_students[i]
        avg = round(sum(cur)/len(cur), 1)
        try:
            dict_final["students_avg"][i].append(avg)
        except:
            dict_final["students_avg"][i] = avg
    best_subject = max([[i, sum(dict_subjects[i])/len(dict_subjects[i])] for i in dict_subjects], key=lambda x: x[1])
    dict_final["best_course"] = best_subject[0]
    return(dict_final)
    pass

# data = [("Алиса", "Математика", 5), ("Борис", "Математика", 4), ("Алиса", "Физика", 4), ("Борис", "Физика", 5)]
# print(analyze_grades(data))
