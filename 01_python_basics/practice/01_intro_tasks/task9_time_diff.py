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

import math

inList = [
    int(input("час прихода:")),
    int(input("минута прихода:")),
    int(input("секунда прихода:")),
    int(input("час ухода:")),
    int(input("минута ухода:")),
    int(input("секунда ухода:")),
    ]

dHours = inList[3] - inList[0]

dMins = inList[4] - inList[1]
dHours += math.floor(dMins/60)
dMins = dMins % 60


dSecs = inList[5] - inList[2]
dMins += math.floor(dSecs / 60)
dSecs = dSecs % 60

print(
    f"{math.fabs(dHours):01.0f}:{(math.fabs(dMins)):02.0f}:{math.fabs((dSecs)):02.0f}"
)