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

both = set(sorted(yesterday.intersection(today)))
only_today = set(sorted(today.difference(yesterday)))
unique = yesterday.union(today)
print("Находили оба дня:", both)
print("Только сегодня:", only_today)
print("Всего уникальных моделей:", len(unique))