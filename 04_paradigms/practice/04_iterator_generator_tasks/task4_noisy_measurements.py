"""
Задание 4: Генератор зашумлённых измерений

Функция noisy_measurements(base_values, noise_level=0.1) — генератор.
Для каждого значения из base_values выдаёт 3 зашумлённых измерения:
value * (1 + random.uniform(-noise_level, noise_level)).
Использует yield для каждого измерения.
"""
