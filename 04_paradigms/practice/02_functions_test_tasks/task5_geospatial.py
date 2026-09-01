"""
Задание 5: Геопространственный анализ

Функция find_least_served_districts(data, n=3) определяет районы с наименьшим количеством
социальных объектов на квадратный километр.
Возвращает список кортежей (район, плотность), отсортированный по возрастанию плотности.
"""

# НАПИШИТЕ ВАШ КОД ЗДЕСЬ
# 04_paradigms/practice/02_functions_test_tasks/task5_geospatial.py


def find_least_served_districts(data, n=3):
    districts = {}
    for obj in data['objects']:
        d = obj['district']
        if d not in districts:
            districts[d] = {'count': 0, 'coords': []}
        districts[d]['count'] += 1
        districts[d]['coords'].append(obj['coordinates'])

    result = []
    for d, info in districts.items():
        coords = info['coords']
        if len(coords) < 2:
            area = 1.0
        else:
            lats = [c[0] for c in coords]
            lons = [c[1] for c in coords]
            area = max(0.01, (max(lats) - min(lats)) * (max(lons) - min(lons)))
        density = info['count'] / area
        result.append((d, round(density, 4)))
    result.sort(key=lambda x: x[1])
    return result[:n]
