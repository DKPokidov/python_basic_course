"""
Задание 4: Статистика по услугам

Функция services_stats(data) собирает все уникальные услуги по типам объектов.
Возвращает словарь {тип: [список_услуг]}.
"""

# НАПИШИТЕ ВАШ КОД ЗДЕСЬ
# 04_paradigms/practice/02_functions_test_tasks/task4_services_stats.py


def services_stats(data):
    result = {}
    for obj in data['objects']:
        obj_type = obj['type']
        if obj_type not in result:
            result[obj_type] = set()
        result[obj_type].update(obj['services'])
    return {k: list(v) for k, v in result.items()}
