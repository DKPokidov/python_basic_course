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
into_hour = int(input('Час прихода: '))
into_min = int(input('Минута прихода: '))
into_sec = int(input('Секунда прихода: '))
out_hour = int(input('Час ухода: '))
out_min = int(input('Минута ухода: '))
out_sec = int(input('Секунда ухода: '))
dif_hour, dif_min, dif_sec = (out_hour - into_hour), str((out_min - into_min)).zfill(2), str((out_sec - into_sec)).zfill(2)
print(f'{dif_hour}:{dif_min}:{dif_sec}') 