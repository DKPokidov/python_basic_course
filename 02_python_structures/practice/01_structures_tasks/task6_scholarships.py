"""
Задание 6: Статистика по стипендиям

В ИТМО подсчитывают статистику по стипендиям студентов.
Нужно проанализировать данные без использования циклов.

1. Найдите максимальную стипендию
2. Найдите минимальную стипендию
3. Посчитайте общую сумму всех стипендий
4. Создайте множество уникальных размеров стипендий
5. Создайте список всех студентов в алфавитном порядке
"""

# НАПИШИТЕ ВАШ КОД ЗДЕСЬ
# 02_python_structures/practice/01_structures_tasks/task6_scholarships.py

# Данные о стипендиях студентов (имя: стипендия)
scholarships = {
    "Мария": 15000,
    "Иван": 12000,
    "Анна": 18000,
    "Петр": 12000,
    "Ольга": 15000
}

max_scholarship = max(scholarships.values())
min_scholarship = min(scholarships.values())
total_scholarships = sum(scholarships.values())
unique_scholarships = set(scholarships.values())
sorted_students = sorted(scholarships.keys())

print("Максимальная стипендия:", max_scholarship)
print("Минимальная стипендия:", min_scholarship)
print("Общая сумма стипендий:", total_scholarships)
print("Уникальные размеры стипендий:", unique_scholarships)
print("Студенты по алфавиту:", sorted_students)
