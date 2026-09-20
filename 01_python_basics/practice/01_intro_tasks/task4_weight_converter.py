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
weight, measure = input("Введите вес и единицу измерения: ").strip().split()
weight = float(weight)
if measure == "кг":
    print(f"{weight} {measure} = {weight:.6f} кг")
elif measure == "г":
    print(f"{weight} {measure} = {(weight * 0.001):.6f} кг")
elif measure == "фунт":
    print(f"{weight} {measure} = {(weight * 0.40951241):.6f} кг") 
elif measure == "пуд":
    print(f"{weight} {measure} = {(weight * 16):.6f} кг") 
elif measure == "ц":
    print(f"{weight} {measure} = {(weight * 100):.6f} кг")
elif measure == "т":
    print(f"{weight} {measure} = {(weight * 1000):.6f} кг")
