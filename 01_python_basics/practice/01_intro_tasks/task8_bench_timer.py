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

userInput = int(input("Введите время в секундах: "))
hours = userInput // 3600
userInput %= 3600
minutes = userInput // 60
userInput %= 60

print(hours, f"{minutes:02d}", f"{userInput:02d}", sep=":")
