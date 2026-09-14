# module_01_python_basics/practice/task8_bench.py
"""
Задание 8: Умные скамейки

Напишите программу, которая:
1. Запрашивает время в секундах
2. Переводит в формат "часы:минуты:секунды"
3. Выводит результат

Пример:
Введите время в секундах: 3661
1:01:01
"""

initial = int(input("Введите время в секундах: "))
hours = initial // 3600
minutes = initial % 3600//60
seconds = initial % 60
print(f"{hours}:" + ["", "0"][minutes < 10] + str(minutes) + ":" + (["", "0"][seconds < 10] + str(seconds)))
