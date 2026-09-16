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
sec = int(input('Введите время в секундах: '))
hours = sec // 3600
minutes = (sec - hours * 3600) // 60
seconds = sec - (hours * 3600 + minutes * 60)
print(f'{hours} : {minutes:02d} : {seconds:02d}')