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

time = int(input("Введите время в секундах:"))
hours = time // 3600
minutes = (time - 3600 * (hours)) // 60
seconds = time - minutes * 60 - hours * 3600
print(f"{hours}:{minutes:02d}:{seconds:02d}")
