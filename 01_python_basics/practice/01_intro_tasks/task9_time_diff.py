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
sec1 = hour1 * 3600 + minute1 * 60 + second1
sec2 = hour2 * 3600 + minute2 * 60 + second2
diff = sec2 - sec1
hours = diff // 3600
minutes = (diff - hours * 3600) // 60
seconds = diff - (hours * 3600 + minutes * 60)
print(f"{hours}:{minutes:02d}:{seconds:02d}")