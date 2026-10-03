"""
Задание 7: Логический тип данных: таблицы истинности

Изучите работу логических операций и выведите таблицы истинности:

1. Конъюнкция (and — логическое умножение)
2. Дизъюнкция (or — логическое сложение)
3. Инверсия (not — логическое отрицание)
"""
print(f"False and False = {False}")
print(f"False and True = {False}")
print(f"True and False = {False}")
print(f"True and True = {True}")

print(f"False or False = {False}")
print(f"False or True = {True}")
print(f"True or False = {True}")
print(f"True or True = {True}")

print(f"not False = {True}")
print(f"not True = {False}")