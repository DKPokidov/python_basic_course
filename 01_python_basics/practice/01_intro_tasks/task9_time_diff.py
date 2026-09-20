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
time_arrival_hour = int(input("Час прихода: "))
time_arrival_minute = int(input("Минута прихода: "))
time_arrival_second = int(input("Секунда прихода: "))
time_departure_hour = int(input("Час ухода: "))
time_departure_minute = int(input("Минута ухода: "))
time_departure_second = int(input("Секунда ухода: "))
raznica=((time_departure_hour - time_arrival_hour) * 3600 + (time_departure_minute - time_arrival_minute) * 60 + (time_departure_second - time_arrival_second))
hours = raznica // 3600
minutes = (raznica % 3600) // 60
seconds = raznica % 60
print(f"{hours}:{minutes}:{seconds}")