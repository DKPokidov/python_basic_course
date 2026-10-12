"""
Задание 7: Логический тип данных: таблицы истинности

Изучите работу логических операций и выведите таблицы истинности:

1. Конъюнкция (and — логическое умножение)
2. Дизъюнкция (or — логическое сложение)
3. Инверсия (not — логическое отрицание)
"""
a = True
b = True
print(a, 'and', b, '=', a and b)
a = True
b = False
print(a, 'and', b, '=', a and b)
a = False
b = True
print(a, 'and', b, '=', a and b)
a = False
b = False
print(a, 'and', b, '=', a and b)
a = True
b = True
print(a, 'or', b, '=', a or b)
a = True
b = False
print(a, 'or', b, '=', a or b)
a = False
b = True
print(a, 'or', b, '=', a or b)
a = False
b = False
print(a, 'or', b, '=', a or b)
a = True
print('not', a, '=', not a)
a = False
print('not', a, '=', not a)
