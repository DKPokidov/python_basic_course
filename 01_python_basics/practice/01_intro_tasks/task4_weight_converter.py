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

userInput = input("Введите вес и единицу измерения (например, '10 кг'): ")
coefficient = 0
numPart =  float(userInput.split(" ")[0])
unitPart = userInput.split(" ")[1]
match unitPart:
    case "кг":
        coefficient = 1
    case "г":
        coefficient = 0.001
    case "фунт":
        coefficient = 0.40951241
    case "пуд":
        coefficient = 16
    case "ц":
        coefficient = 100
    case "т":
        coefficient = 1000
    case _:
        print("Error")
        exit

print(userInput, " = ", numPart * coefficient, "кг")
