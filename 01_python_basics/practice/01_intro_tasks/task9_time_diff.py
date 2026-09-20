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
hours1 = int(input("Час прихода:"))
minutes1 = int(input("Минута прихода:"))
seconds1 = int(input("Секунда прихода:"))
hours2 = int(input("Час ухода:"))
minutes2 = int(input("Минута ухода:"))
seconds2 = int(input("Секунда ухода:"))
time1 = seconds1 + minutes1*60 + hours1*3600
time2 = seconds2 + minutes2*60 + hours2*3600
time = time2-time1
hours = time//3600
minutes = (time-3600*(hours))//60
seconds = time-minutes*60-hours*3600
print(f"{hours}:{minutes:02d}:{seconds:02d}")
