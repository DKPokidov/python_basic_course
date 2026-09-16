# module_01_python_basics/practice/task4_functions.py
"""
Задание 4: Международный весооборот

Напишите программу, которая:
1. Запрашивает вес и единицу измерения (кг, г, фунт, пуд, ц, т)
2. Переводит вес в килограммы
3. Выводит: "{вес} {единица} = {результат} кг"

Коэффициенты перевода в кг:
- 1 кг = 1 кг
- 1 г = 0.001 кг
- 1 фунт = 0.40951241 кг
- 1 пуд = 16 кг
- 1 ц = 100 кг
- 1 т = 1000 кг

Пример:
Введите вес и единицу измерения (например, '10 кг'): 1 т
1.0 т = 1000.000000 кг
"""

weight, bukva = input("Введите вес и единицу измерения (например, '10 кг'): ").strip().split()

if bukva == 'кг':
    print(f'{weight} кг = {weight} кг')
elif bukva == 'г':
    print(f'{float(weight)} г = {(float(weight) * 10**-3):.6f} кг')
elif bukva == 'пуд':
    print(f'{float(weight)} пуд = {(float(weight) * 16):.6f} кг')
elif bukva == 'фунт':
    print(f'{float(weight)} фунт = {(float(weight) * 0.40951241):.6f} кг')
elif bukva == 'ц':
    print(f'{float(weight)} ц = {(float(weight) * 100):.6f} кг')
elif bukva == 'т':
    print(f'{float(weight)} т = {(float(weight) * 1000):.6f} кг')
