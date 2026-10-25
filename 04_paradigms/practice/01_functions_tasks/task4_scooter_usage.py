"""
Задание 4: Анализ использования городских электросамокатов

Вы аналитик сервиса кикшеринга. С парка самокатов приходит журнал поездок:
для каждой записи — пользователь, длительность в минутах, дистанция
в километрах и стартовая зона. Компания хочет понимать, с какой скоростью
в среднем ездят клиенты, — особенно в зонах, где установлен лимит скорости.

Напишите функцию analyze_scooter_usage(data):
- Вход: list of dicts {"user_id": int, "duration_min": int,
                       "distance_km": float, "start_zone": str}
- Исходные словари не меняйте: для каждой поездки создайте копию
  с добавленным полем
    speed_kmh = round((distance_km / duration_min) * 60, 1)
  Если duration_min == 0 (поездку «забыли» закрыть приложением) —
  считайте speed_kmh = 0.0.
- Возвращает list of новых dicts с добавленным полем speed_kmh.
"""


def analyze_scooter_usage(data):
    new_data = list()
    for line in data:
        distance_km = line['distance_km']
        duration_min = line['duration_min']
        speed_kmh = 0.0
        if duration_min != 0:
            speed_kmh = round((distance_km / duration_min) * 60, 1)
        new_line = line.copy()
        new_line['speed_kmh'] = speed_kmh
        new_data.append(new_line)
    return new_data
