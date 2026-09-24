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
minute1 = int(input('Минута прихода: '))
second1 = int(input('Секунда прихода: '))
hour2 = int(input('Час ухода: '))
minute2 = int(input('Минута ухода: '))
second2 = int(input('Секунда ухода: '))
come = hour1 * 3600 + minute1 * 60 + second1
leave = hour2 * 3600 + minute2 * 60 + second2
time = leave - come
hour = time // 3600
second = time % 60
minute = (time - hour * 3600 - second) // 60
second = f"{second:02d}"
minute = f"{minute:02d}"
print(hour, minute, second, sep=':')
