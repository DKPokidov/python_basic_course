# tests/test_module09/test_task3_prime_iterator.py
"""
Тесты для задания 3: Итератор простых чисел
"""

import importlib.util
from tests.test_module09.conftest import get_module09_file


def load_student_code(student_file):
    spec = importlib.util.spec_from_file_location("student_module", student_file)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class TestTask3PrimeIterator:
    """Тесты для задания 3: Итератор простых чисел"""

    student_file = get_module09_file('task3_prime_iterator.py')

    def test_is_iterable(self):
        mod = load_student_code(self.student_file)
        it = mod.PrimeIterator(1, 10)
        assert hasattr(it, '__iter__')
        assert hasattr(it, '__next__')
        assert iter(it) is it

    def test_primes_1_to_10(self):
        mod = load_student_code(self.student_file)
        result = list(mod.PrimeIterator(1, 10))
        assert result == [2, 3, 5, 7]

    def test_primes_10_to_20(self):
        mod = load_student_code(self.student_file)
        result = list(mod.PrimeIterator(10, 20))
        assert result == [11, 13, 17, 19]

    def test_primes_2_to_3(self):
        mod = load_student_code(self.student_file)
        result = list(mod.PrimeIterator(2, 3))
        assert result == [2]

    def test_primes_empty_range(self):
        mod = load_student_code(self.student_file)
        result = list(mod.PrimeIterator(1, 1))
        assert result == []

    def test_primes_20_to_30(self):
        mod = load_student_code(self.student_file)
        result = list(mod.PrimeIterator(20, 30))
        assert result == [23, 29]
