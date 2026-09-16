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
chas1=int(input('Час прихода:'))
min1=int(input('Минута прихода:'))
sek1=int(input('Секунда прихода:'))
chas2=int(input('Час ухода:'))
min2=int(input('Минута ухода:'))
sek2=int(input('Секунда ухода:'))
vremya1 = chas1 * 3600 + min1 * 60 + sek1
vremya2 = chas2 * 3600 + min2 * 60 + sek2
if vremya2 > vremya1:
    vremya = vremya2 - vremya1
    
if vremya1 > vremya2:
    vremya = ( 24*3600 - vremya1 ) + vremya2
    
chas=vremya//3600
min= ( vremya - (chas * 3600)) // 60
sek=(vremya - (min * 60))%3600
if min<10:
    min='0'+str(min)
if sek<10:
    sek='0'+str(sek)
print(f'{chas} : {min} : {sek}')