"""
Задание 2: Анализ доступности

Функция accessibility_analysis(data) подсчитывает количество объектов с ramp == True в каждом районе.
Возвращает словарь {район: количество_доступных_объектов}.
"""

# НАПИШИТЕ ВАШ КОД ЗДЕСЬ
# 04_paradigms/practice/02_functions_test_tasks/task2_accessibility_analysis.py


def accessibility_analysis(data):
    result = {}
    for obj in data['objects']:
        if obj['accessibility']['ramp']:
            district = obj['district']
            result[district] = result.get(district, 0) + 1
    return result
