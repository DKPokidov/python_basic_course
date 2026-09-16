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
time = int(input('Введите время в секундах: '))
hour = time // 3600
minuts = (time - hour * 3600) // 60
sekunds = time - hour * 3600 - minuts * 60
if minuts < 10 and sekunds < 10:
    print(f'{hour}:0{minuts}:0{sekunds}')
elif minuts < 10 and sekunds >= 10:
    print(f'{hour}:0{minuts}:{sekunds}')
elif minuts >= 10 and sekunds < 10:
    print(f'{hour}:{minuts}:0{sekunds}')
else:
    print(f'{hour}:{minuts}:{sekunds}')



