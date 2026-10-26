"""
Задание 7: Логический тип данных: таблицы истинности

Изучите работу логических операций и выведите таблицы истинности:

1. Конъюнкция (and — логическое умножение)
2. Дизъюнкция (or — логическое сложение)
3. Инверсия (not — логическое отрицание)
"""
tablica_and = [[True, True, True], [True, False, False], [False, True, False], [False, False, False]]
tablica_or = [[True, True, True], [True, False, True], [False, True, True], [False, False, False]]
tablica_not = [[True, False], [False, True]]
print("Таблица истинности для конъюнкции (and):")
for row in tablica_and:
    print(row)
print("Таблица истинности для дизъюнкции (or):")
for row in tablica_or:
    print(row)
print("Таблица истинности для инверсии (not):")
for row in tablica_not:
    print(row)