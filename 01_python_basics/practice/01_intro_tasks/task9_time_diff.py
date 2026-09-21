# module_01_python_basics/practice/task9_time.py
"""
Задание 9: Счастливых часов не наблюдают

Напишите программу, которая:
1. Запрашивает время прихода (часы, минуты, секунды)
2. Запрашивает время ухода (часы, минуты, секунды)
3. Вычисляет разницу во времени
4. Выводит в формате "часы:минуты:секунды"

Пример:
Час прихода: 9
Минута прихода: 0
Секунда прихода: 0
Час ухода: 12
Минута ухода: 30
Секунда ухода: 0
3:30:00
"""

arrival_hour = int(input("Час прихода: "))
arrival_minute = int(input("Минута прихода: "))
arrival_second = int(input("Секунда прихода: "))
departure_hour = int(input("Час ухода: "))
departure_minute = int(input("Минута ухода: "))
departure_second = int(input("Секунда ухода: "))
pure_1 = arrival_hour * 3600 + arrival_minute * 60 + arrival_second
pure_2 = departure_hour * 3600 + departure_minute * 60 + departure_second
initial = pure_2 - pure_1
hours = initial // 3600
minutes = initial % 3600 // 60
seconds = initial % 60
print(f"{hours}:" + ["", "0"][minutes < 10] + str(minutes) + ":" + (["", "0"][seconds < 10] + str(seconds)))
