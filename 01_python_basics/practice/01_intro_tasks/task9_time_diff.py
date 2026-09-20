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
hours0 = int(input("Час прихода: "))
mins0 = int(input("Минута прихода: "))
sec0 = int(input("Секунда прихода: "))
hours1 = int(input("Час ухода: "))
mins1 = int(input("Минута ухода: "))
sec1 = int(input("Секунда ухода: "))
hours_total = hours1-hours0
mins_total = mins1-mins0
sec_total = sec1 - sec0
if sec_total < 0 :
    mins_total = mins_total - 1 
    sec_total = 60 + sec_total
if mins_total < 0 :
    hours_total = hours_total - 1
    mins_total = 60 + mins_total
print(f"{hours_total}:{mins_total :02}:{sec_total :02}")