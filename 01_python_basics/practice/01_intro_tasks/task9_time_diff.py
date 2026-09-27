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
came_hour = int(input('Час прихода: '))
came_minute = int(input('Минута прихода: '))
came_second = int(input('Секунда прихода: '))
go_hour = int(input('Час ухода: '))
go_minute = int(input('Минута ухода: '))
go_second = int(input('Секунда ухода: '))
came_time = came_hour * 3600 + came_minute * 60 + came_second
go_time = go_hour * 3600 + go_minute * 60 + go_second
time = go_time - came_time
print (f'{time // 3600}:{((time % 3600)// 60):02d}:{(time % 60):02d}')

