"""
Задание 7: Логический тип данных: таблицы истинности

Изучите работу логических операций и выведите таблицы истинности:

1. Конъюнкция (and — логическое умножение)
2. Дизъюнкция (or — логическое сложение)
3. Инверсия (not — логическое отрицание)
"""

# НАПИШИТЕ ВАШ КОД ЗДЕСЬ
# 02_python_structures/practice/01_structures_tasks/task7_truth_tables.py

# Конъюнкция (логическое умножение)
print(f'False and False = {False and False}')
print(f'False and True = {False and True}')
print(f'True and False = {True and False}')
print(f'True and True = {True and True}')

# Дизъюнкция (логическое сложение)
print(f'False or False = {False or False}')
print(f'False or True = {False or True}')
print(f'True or False = {True or False}')
print(f'True or True = {True or True}')

# Инверсия (логическое отрицание)
print(f'not False = {not False}')
print(f'not True = {not True}')
