"""
Задание 7: Логический тип данных: таблицы истинности

Изучите работу логических операций и выведите таблицы истинности:

1. Конъюнкция (and — логическое умножение)
2. Дизъюнкция (or — логическое сложение)
3. Инверсия (not — логическое отрицание)
"""

for a in range(2):
    for b in range(2):
        print(f"{bool(a)} and {bool(b)} = {bool(a and b)}")

for a in range(2):
    for b in range(2):
        print(f"{bool(a)} or {bool(b)} = {bool(a or b)}")

for a in range(2):
    print(f"not {bool(a)} = {not a}")
