"""
Задание 7: Логический тип данных: таблицы истинности

Изучите работу логических операций и выведите таблицы истинности:

1. Конъюнкция (and — логическое умножение) оба верные для истины
2. Дизъюнкция (or — логическое сложение) хотя бы одно верное
3. Инверсия (not — логическое отрицание) 
"""
print(f"True and True = {True and True}")
print(f"True and False = {True and False}")
print(f"False and True = {False and True}")
print(f"False and False = {False and False}")

print(f"True or True = {True or True}")
print(f"True or False = {True or False}")
print(f"False or True = {False or True}")
print(f"False or False = {False or False}")

print(f"not True = {not True}")
print(f"not False = {not False}")