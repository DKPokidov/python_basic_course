# module_01_python_basics/practice/task8_bench.py
"""
Задание 8: Умные скамейки

Напишите программу, которая:
1. Запрашивает время в секундах
2. Переводит в формат "часы:минуты:секунды"
3. Выводит результат

Пример:
Введите время в секундах: 3661
1:01:01
"""
vremya=int(input('Введите время в секундах:'))
chas=vremya//3600
min= ( vremya - (chas * 3600)) // 60
sek=(vremya - (min * 60))%3600
if min<10:
    min='0'+str(min)
if sek<10:
    sek='0'+str(sek)
print(f'{chas} : {min} : {sek}')
