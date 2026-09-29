"""
Задание 2: Поиск потерянных наушников

В кампусе ИТМО постоянно теряют наушники. Создайте систему для отслеживания находок!
Данные о находках за два дня уже заданы.

Пример вывода:
1. Находили оба дня: {'беспроводные Sony'}
2. Только сегодня: {'Samsung Buds', 'старые советские'}
3. Всего уникальных моделей: 5
"""

yesterday = {"беспроводные Sony", "AirPods", "JBL"}
today = {"беспроводные Sony", "Samsung Buds", "старые советские"}

finds_both_days = yesterday & today 
finds_only_today = today.difference(yesterday)
finds_amount = len(yesterday.union(today))

print(f"Находили оба дня: {finds_both_days}")
print(f"Только сегодня: {finds_only_today}")
print(f"Всего уникальных моделей: {finds_amount}")
