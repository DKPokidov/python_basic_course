"""
Задание 7: Логический тип данных: таблицы истинности

Изучите работу логических операций и выведите таблицы истинности:

1. Конъюнкция (and — логическое умножение)
2. Дизъюнкция (or — логическое сложение)
3. Инверсия (not — логическое отрицание)
"""

import math as m
import numpy as np

def bool_table(operation):
    table = f'x y res \n'
    for x in range(2):
        for y in range(2):
            line = ''
            line += f'{x} {y} {operation(x, y)} \n'
            table += line

    print(table)

def conjunction(x, y):
    return x * y

def disjunction(x, y):
    return int(np.clip(x + y, 0, 1))

def inversion():
    for x in range(2):
        print(f'{x} {not x}')

bool_table(conjunction)
bool_table(disjunction)        
inversion()