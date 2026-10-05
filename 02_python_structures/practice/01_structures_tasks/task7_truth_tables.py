"""
Задание 7: Логический тип данных: таблицы истинности

Изучите работу логических операций и выведите таблицы истинности:

1. Конъюнкция (and — логическое умножение)
2. Дизъюнкция (or — логическое сложение)
3. Инверсия (not — логическое отрицание)
"""

for x in (False, True):
    for y in (False, True):
        print(bool(x), "and", bool(y), "=", bool(x and y))

for x in (False, True):
    for y in (False, True):
        print(bool(x), "or", bool(y), "=", bool(x or y))

for x in (False, True):
    print("not", x, "=", bool(not x))
