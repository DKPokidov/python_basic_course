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
    new_list = []
    for travel in data:
        new_data = travel.copy()
        if new_data['duration_min'] == 0:
            speed_kmh = 0.0
        else:
            speed_kmh = round((new_data['distance_km'] / new_data['duration_min']) * 60, 1)    
        new_data.update(
            {
            'speed_kmh': speed_kmh
            }
        )
        new_list.append(new_data)
    return new_list
    
        
        

    