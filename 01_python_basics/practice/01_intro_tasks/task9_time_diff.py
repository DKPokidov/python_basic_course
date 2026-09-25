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

hourCame = int(input("Час прихода: "))
minuteCame = int(input("Минута прихода: "))
secondCame = int(input("Секунда прихода: "))
hourLeft = int(input("Час ухода: "))
minuteLeft = int(input("Минута ухода: "))
secondLeft = int(input("Секунда ухода: "))

timestampCame = hourCame * 3600 + minuteCame * 60 + secondCame
timestampLeft = hourLeft * 3600 + minuteLeft * 60 + secondLeft

timeSpent = timestampLeft - timestampCame

hoursSpent = timeSpent // 3600
timeSpent %= 3600
minutesSpent = timeSpent // 60
timeSpent %= 60

print(hoursSpent, f"{minutesSpent:02d}", f"{timeSpent:02d}", sep=":")