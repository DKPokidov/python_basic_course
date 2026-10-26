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

def analyze_grades(data: list[tuple[str, str, float]]) -> dict:

    dict_byCourse: dict = {}
    dict_studentAverages: dict = {}

    for each in data:
        if dict_byCourse.get(each[1]) == None:
            dict_byCourse[each[1]] = [[], 0]

        dict_byCourse[each[1]][0] += [each]

    for each in dict_byCourse.items():
        each[1][1] = sum(
            map((lambda x: float(x[2])), each[1][0])
        ) / len(each[1][0])

    for each in data:
        if (dict_studentAverages.get(each[0]) == None):
            dict_studentAverages[each[0]] = [[], 0]

        dict_studentAverages[each[0]][0] += [each]

    for each in dict_studentAverages.items():
        each[1][1] = sum(
            map((lambda x: float(x[2])), each[1][0])
        ) / len(each[1][0])

    return {
        'students_avg': {each[0]:each[1][1] for each in dict_studentAverages.items()},
        'best_course': (
            max(dict_byCourse.items(), key=(lambda x: x[1][1]))[0]
        )
    }
    