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
t = int(input("Введите время в секундах:"))
hour = t//3600
minute = t%3600//60
sek = t%60
if minute < 10 and sek < 10:
    print(hour, ":0", minute, ":0", sek, sep = "")
elif minute < 10 and sek >= 10:
    print(hour, ":0", minute, ":", sek, sep = "")
elif minute >= 10 and sek < 10:
    print(hour, ":0", minute, ":0", sek, sep = "")
else:
    print(hour, minute, sek, sep=":")
