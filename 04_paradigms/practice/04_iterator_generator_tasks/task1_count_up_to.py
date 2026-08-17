"""
Задание 1: Генератор натуральных чисел

Функция count_up_to(n) — генератор, который выдаёт числа от 1 до n включительно через yield.
"""

# НАПИШИТЕ ВАШ КОД ЗДЕСЬ
# 04_paradigms/practice/04_iterator_generator_tasks/task1_count_up_to.py


def count_up_to(n):
    for i in range(1, n + 1):
        yield i
