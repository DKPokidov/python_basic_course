"""
Задание 3: Итератор простых чисел

Класс PrimeIterator(start, end) — итератор, возвращающий все простые числа в диапазоне [start, end).
"""

# НАПИШИТЕ ВАШ КОД ЗДЕСЬ
# 04_paradigms/practice/04_iterator_generator_tasks/task3_prime_iterator.py


class PrimeIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        while self.current < self.end:
            if self.is_prime(self.current):
                result = self.current
                self.current += 1
                return result
            self.current += 1
        raise StopIteration

    def is_prime(self, num):
        if num < 2:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        for i in range(3, int(num**0.5) + 1, 2):
            if num % i == 0:
                return False
        return True
