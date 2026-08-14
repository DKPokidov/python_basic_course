"""
Задание 6: Измеряем улицы

Найти количество городов с длиной улиц больше 400 км.
"""

# НАПИШИТЕ ВАШ КОД ЗДЕСЬ
# 03_control_flow/practice/01_control_flow_tasks/task6_streets.py

cities_list = [
    {'city': 'Москва', 'streets_length': 567},
    {'city': 'Санкт-Петербург', 'streets_length': 453},
    {'city': 'Псков', 'streets_length': 123},
    {'city': 'Калининград', 'streets_length': 324},
    {'city': 'Челябинск', 'streets_length': 409}
]

min_length = 400  # минимальная длина дорог

total_count = 0  # заводим переменную для количества городов
for city_dict in cities_list:
    if city_dict['streets_length'] > min_length:
        total_count += 1

print(f'Городов с длинной дорог большей, чем {min_length} = {total_count}')
