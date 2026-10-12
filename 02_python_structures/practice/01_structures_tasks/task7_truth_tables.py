"""
Задание 7: Логический тип данных: таблицы истинности

Изучите работу логических операций и выведите таблицы истинности:

1. Конъюнкция (and — логическое умножение)
2. Дизъюнкция (or — логическое сложение)
3. Инверсия (not — логическое отрицание)
"""
print(f'Конъюнкция')
for a in (True, False):
    for b in (True, False):
        print(f'{a} and {b} = {a and b}')

print(f'Дизъюнкция')
for a in (True, False):
    for b in (True, False):
        print(f'{a} or {b} = {a or b}')

print(f'Инверсия')
for a in (True, False):
    print(f'not {a} = {not a}')
