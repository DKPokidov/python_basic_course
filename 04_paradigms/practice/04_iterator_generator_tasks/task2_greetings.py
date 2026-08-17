"""
Задание 2: Генератор приветствий

Функция greetings(names) — генератор, выдаёт строки "Привет, {имя}!" для каждого имени из списка names.
"""

# НАПИШИТЕ ВАШ КОД ЗДЕСЬ
# 04_paradigms/practice/04_iterator_generator_tasks/task2_greetings.py


def greetings(names):
    for name in names:
        yield f"Привет, {name}!"
