"""
Задание 4: Анализ использования городских электросамокатов

Функция analyze_scooter_usage(data):
- Вход: list of dicts {"user_id": int, "duration_min": int, "distance_km": float, "start_zone": str}
- Добавляет speed_kmh = round((distance_km / duration_min) * 60, 1) или 0.0 если duration_min == 0
- Возвращает list of dicts с добавленным полем speed_kmh
"""


def analyze_scooter_usage(data):
    pass