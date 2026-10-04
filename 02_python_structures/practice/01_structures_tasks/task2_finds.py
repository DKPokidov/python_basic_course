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

unique_models = yesterday.union(today)
both_days_finds = yesterday.intersection(today)
only_today_finds = today.difference(yesterday)

print(f'Находили оба дня: {both_days_finds}')
print(f'Только сегодня: {only_today_finds}')
print(f'Всего уникальных моделей: {len(unique_models)}')

