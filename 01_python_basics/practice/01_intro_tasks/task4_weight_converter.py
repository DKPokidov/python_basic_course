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
base_input = input("Введите вес и единицу измерения (например, '10 кг'): ")
weight, unit = base_input.split()
weight = float(weight)
unit = unit.lower()
if unit == "кг":
    result = weight
elif unit == "г":
    result = weight * 0.001
elif unit == "фунт":
    result = weight * 0.40951241
elif unit == "пуд":
    result = weight * 16
elif unit == "ц":
    result = weight * 100
elif unit == "т":
    result = weight * 1000

print(f"{weight} {unit} = {result} кг")