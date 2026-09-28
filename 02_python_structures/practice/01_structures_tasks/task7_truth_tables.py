"""
Задание 7: Логический тип данных: таблицы истинности

Изучите работу логических операций и выведите таблицы истинности:

1. Конъюнкция (and — логическое умножение)
2. Дизъюнкция (or — логическое сложение)
3. Инверсия (not — логическое отрицание)
"""

andTable = ((0, 0), (0, 1))
orTable = ((0, 1), (1, 1))
notTable = (1, 0)

print("False and False = False\nFalse and True = False\nTrue and False = False\nTrue and True = True")
print("False or False = False\nFalse or True = True\nTrue or False = True\nTrue or True = True")
print("not False = True\nnot True = False")
