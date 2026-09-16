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
arrival_hours = int(input("Час прихода: "))*3600
arrival_minutes = int(input("Минута прихода: "))*60
arrival_seconds = int(input("Секунда прихода: "))
departure_hours = int(input("Час ухода: "))*3600
departure_minutes = int(input("Минута ухода: "))*60
departure_seconds = int(input("Секунда ухода: "))
total_time = (departure_hours + departure_minutes + departure_seconds) - (arrival_hours + arrival_minutes + arrival_seconds)
print(f'{total_time//3600}:{total_time//60%60:02}:{total_time%60:02}')