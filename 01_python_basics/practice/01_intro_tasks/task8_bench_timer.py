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
print("Введите время в секундах: ")
total_seconds = int(input())
hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60
print(f"{hours}:{minutes:02}:{seconds:02}")
