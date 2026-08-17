"""
Задание 4: Генератор зашумлённых измерений

Функция noisy_measurements(base_values, noise_level=0.1) — генератор.
Для каждого значения из base_values выдаёт 3 зашумлённых измерения:
value * (1 + random.uniform(-noise_level, noise_level)).
Использует yield для каждого измерения.
"""

# НАПИШИТЕ ВАШ КОД ЗДЕСЬ
# 04_paradigms/practice/04_iterator_generator_tasks/task4_noisy_measurements.py


import random


def noisy_measurements(base_values, noise_level=0.1):
    for value in base_values:
        for _ in range(3):
            deviation = random.uniform(-noise_level, noise_level)
            yield value * (1 + deviation)
