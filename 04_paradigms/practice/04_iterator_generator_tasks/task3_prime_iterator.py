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

def prime(x):
    f = 1
    for i in range(2, int(x**.5) + 1):
        if x % i == 0:
            f = 0
    return f and (x != 1)


class PrimeIterator:
    def __init__(self, start, end):
        self.cur = start
        self.end = end
        pass

    def __iter__(self):
        return self
        pass

    def __next__(self):
        while self.cur < self.end:
            if prime(self.cur):
                result = self.cur
                self.cur += 1
                return result
            self.cur += 1 
        raise StopIteration
        pass


print(*PrimeIterator(1, 20))