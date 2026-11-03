"""
Задание 3: Итератор простых чисел

Криптограф подбирает простые множители в заданном диапазоне чисел.
Перебирать их все сразу — дорого: простые числа нужны ему по одному,
следующее — только после того, как обработано предыдущее. Эту задачу
решает итератор: объект, который хранит состояние (где мы остановились)
и умеет выдать следующий элемент по требованию.

Создайте класс PrimeIterator(start, end) — итератор, возвращающий все
простые числа в диапазоне [start, end) (end не включается). При каждом
обращении к нему вы должны получить следующее простое число, а когда
числа закончатся — исключение StopIteration. Реализуйте методы __iter__(),
__next__() и __init__(self, start, end).
"""


def checkPrime(num: int):
    for divisor in range(2, num):
        if (num % divisor == 0):
            return False
    return True

class PrimeIterator:

    


    def __init__(self, start, end):
        self.current = start if start > 2 else 2
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        while self.current < self.end:
            if (checkPrime(self.current)):
                self.current += 1
                return self.current - 1
            self.current += 1
        raise StopIteration

for x in PrimeIterator(0, 10):
    print(x)