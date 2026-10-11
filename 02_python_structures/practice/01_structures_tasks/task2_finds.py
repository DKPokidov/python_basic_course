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
both_days = yesterday.intersection(today)
only_today = today - yesterday
unic_models = yesterday.union(today)
len_unic = len(unic_models)

print(f"Находили оба дня: {both_days}")
print(f"Только сегодня: {only_today}")
print(f"Всего уникальных моделей: {len_unic}")
