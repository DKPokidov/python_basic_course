"""
Задание 3: Анализ загруженности городских парков

Функция analyze_parks(data, threshold=50):
- data: dict {name: {"visitors_day": int, "area_ha": int, "entrances": int}}
- Возвращает dict {name: {"density": round(visitors/area, 1), "entrance_load": round(visitors/entrances), "status": "перегружен"/"в норме"}}
"""

# НАПИШИТЕ ВАШ КОД ЗДЕСЬ
# 04_paradigms/practice/01_functions_tasks/task3_park_analysis.py


def analyze_park(data, threshold=50):
    result = {}
    for name, info in data.items():
        density = info['visitors_day'] / info['area_ha']
        entrance_load = info['visitors_day'] / info['entrances']
        status = 'перегружен' if density > threshold else 'в норме'
        result[name] = {'density': round(density, 1), 'entrance_load': round(entrance_load), 'status': status}
    return result
