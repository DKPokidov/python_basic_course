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
start = int(input('Введите время в секундах: '))
hours = start // 3600
start = start - hours * 3600
minutes = start // 60 
start = start - minutes * 60
seconds = start
print(f'{hours}:{minutes:02d}:{seconds:02d}')
