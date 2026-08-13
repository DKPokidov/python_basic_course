"""
Задание 2: Поиск потерянных наушников

В кампусе ИТМО постоянно теряют наушники. Создайте систему для отслеживания находок!

Пример вывода:
1. Находили оба дня: {'беспроводные Sony'}
2. Только сегодня: {'Samsung Buds', 'старые советские'}
3. Всего уникальных моделей: 5
"""

# НАПИШИТЕ ВАШ КОД ЗДЕСЬ
# 02_python_structures/practice/01_structures_tasks/task2_finds.py

# Вчерашние находки
yesterday_finds = {"AirPods", "черные проводные", "беспроводные Sony"}
# Сегодняшние находки
today_finds = {"беспроводные Sony", "Samsung Buds", "старые советские"}

# Находим пересечение (находили оба дня)
both_days = yesterday_finds & today_finds
print("Находили оба дня:", both_days)

# Находим разницу (только сегодня)
only_today = today_finds - yesterday_finds
print("Только сегодня:", only_today)

# Объединяем множества
all_finds = yesterday_finds | today_finds
print("Всего уникальных моделей:", len(all_finds))
