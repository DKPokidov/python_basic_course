"""
Задание 4: Анализ студенческих бюджетов

Исследуем, на что тратят деньги студенты в течение недели.

1. Сохраните траты в кортеж
2. Рассчитайте общую сумму трат
3. Найдите самую большую трату
"""

# НАПИШИТЕ ВАШ КОД ЗДЕСЬ
# 02_python_structures/practice/01_structures_tasks/task4_expenses.py

# Программа запрашивает у пользователя траты за неделю
food = float(input("Сколько потратили на еду? "))
transport = float(input("Сколько на транспорт? "))
coffee = float(input("Сколько на кофе? "))
stationery = float(input("Сколько на канцелярию? "))

# Сохраняем траты в кортеж
expenses = (food, transport, coffee, stationery)

# Рассчитываем общую сумму
total = sum(expenses)

# Находим максимальную трату
max_expense = max(expenses)

# Определяем, на что потратили больше всего
categories = ["еда", "транспорт", "кофе", "канцелярию"]
max_category = categories[expenses.index(max_expense)]

print(f"Ваши траты: {expenses}")
print(f"Общая сумма: {total}")
print(f"Самая большая трата: {max_expense} ({max_category} - вот главная статья расходов!)")
