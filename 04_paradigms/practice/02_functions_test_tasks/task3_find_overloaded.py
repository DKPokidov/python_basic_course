"""
Задание 3: Поиск перегруженных объектов

Функция find_overloaded(data, threshold) находит объекты, где capacity > threshold.
Возвращает список строк "{name} ({capacity} мест)".
"""

# НАПИШИТЕ ВАШ КОД ЗДЕСЬ
# 04_paradigms/practice/02_functions_test_tasks/task3_find_overloaded.py


def find_overloaded(data, threshold):
    result = []
    for obj in data['objects']:
        if obj['capacity'] > threshold:
            result.append(f"{obj['name']} ({obj['capacity']} мест)")
    return result
