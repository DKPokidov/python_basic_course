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
time = int(input('Введите время в секундах: '))
hour = time // 3600
second = time % 60
minute = (time - hour * 3600 - second) // 60
second = f"{second:02d}"
minute = f"{minute:02d}"
print(hour, minute, second, sep=':')
