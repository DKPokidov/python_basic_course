"""
Задание 1: Фильтрация по типу объекта

Написать функцию filter_by_type(data, obj_type), которая принимает словарь data и строку obj_type
(например, "school"), возвращает список названий объектов заданного типа.
"""

# НАПИШИТЕ ВАШ КОД ЗДЕСЬ
# 04_paradigms/practice/02_functions_test_tasks/task1_filter_by_type.py


def filter_by_type(data, obj_type):
    return [obj['name'] for obj in data['objects'] if obj['type'] == obj_type]
