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
import math


def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    limitOfCheck = int(math.sqrt(n)) + 1
    for i in range(3, limitOfCheck, 2):
        if n % i == 0:
            return False

    return True


class PrimeIterator:
    cursor = 0
    end = 0
    
    def __init__(self, start, end):
        self.cursor = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        while self.cursor < self.end:
            if isPrime(self.cursor):
                self.cursor += 1
                return self.cursor - 1
            self.cursor += 1
        raise StopIteration
