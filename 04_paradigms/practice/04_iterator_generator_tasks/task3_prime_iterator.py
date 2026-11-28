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
        while self.current < self.end:
            number = self.current
            self.current += 1
            if number < 2:
                continue
            is_prime_number = True
            for i in range(2, number):
                if number % i == 0:
                    is_prime_number = False
                    break
            if is_prime_number:
                return number
        raise StopIteration

        
