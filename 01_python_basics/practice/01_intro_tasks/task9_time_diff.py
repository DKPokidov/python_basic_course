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

print("Час прихода: ")
arrival_hour = int(input())
print("Минута прихода: ")
arrival_minute = int(input())
print("Секунда прихода: ")
arrival_second = int(input())
print("Час ухода: ")
departure_hour = int(input())
print("Минута ухода: ")
departure_minute = int(input())
print("Секунда ухода: ")
departure_second = int(input())
diff_hour = abs(departure_hour - arrival_hour)
diff_minute = abs(departure_minute - arrival_minute)
diff_second = abs(departure_second - arrival_second)
print(f"{diff_hour}:{diff_minute:02}:{diff_second:02}")
