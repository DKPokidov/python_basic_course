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

hour1 = int(input('Час прихода: '))
min1 = int(input('Минута прихода: '))
sec1 = int(input('Секунда прихода: '))
hour2 = int(input('Час ухода: '))
min2 = int(input('Минута ухода: '))
sec2 = int(input('Секунда ухода: '))
t2 = hour2*3600 + min2*60 + sec2
t1 = hour1*3600 + min1*60 + sec1
time = t2 - t1
hours = time//3600
minutes = (time-hours*3600) // 60
sec = time - hours*3600 - minutes*60
if minutes < 10:
    minutes = '0' + str(minutes)
if sec < 10:
    sec = '0' + str(sec)
print(f'{hours}:{minutes}:{sec}')

