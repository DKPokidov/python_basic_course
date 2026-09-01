"""
Задание 3: Анализ загруженности городских парков

Функция analyze_parks(data, threshold=50):
- data: dict {name: {"visitors_day": int, "area_ha": int, "entrances": int}}
- Возвращает dict {name: {"density": round(visitors/area, 1), "entrance_load": round(visitors/entrances), "status": "перегружен"/"в норме"}}
"""
