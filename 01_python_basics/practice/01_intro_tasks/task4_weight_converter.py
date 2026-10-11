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

print("Введите вес и единицу измерения (например, '10 кг'): ")
weight_input = input()
weight_parts = weight_input.split()
weight_value = float(weight_parts[0])
unit = weight_parts[1]
if unit == "кг":
    weight_kg = weight_value
elif unit == "г":
    weight_kg = weight_value * 0.001
elif unit == "фунт":
    weight_kg = weight_value * 0.40951241
elif unit == "пуд":
    weight_kg = weight_value * 16
elif unit == "ц":
    weight_kg = weight_value * 100
elif unit == "т":
    weight_kg = weight_value * 1000
print(f"{weight_value} {unit} = {weight_kg:.6f} кг")
