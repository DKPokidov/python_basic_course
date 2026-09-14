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
hour_arrive = int(input('Час прихода: '))
minut_arrive = int(input('Минута прихода: '))
sec_arrive = int(input('Секунда прихода: '))
hour_out = int(input('Час ухода: '))
minut_out = int(input('Минута ухода: '))
sec_out = int(input('Секунда ухода: '))
tim_arrive = hour_arrive*60*60 + minut_arrive*60 + sec_arrive
tim_out = hour_out*60*60 + minut_out*60 + sec_out
tim = tim_out-tim_arrive
print(f'{tim//(60*60)}:{(tim%(60*60))//60:02d}:{tim%60:02d}')