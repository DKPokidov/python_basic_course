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


class PrimeIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        while not self.is_prime() or self.current == 1:
            self.current += 1
        if self.current >= self.end:
            raise StopIteration
        result = self.current
        self.current += 1
        return result

    def is_prime(self):
        dels = [x for x in range(2, self.current) if self.current % x == 0]
        return True if dels == [] else False
