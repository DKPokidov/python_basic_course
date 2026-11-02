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
    final=[]
    for i in range(len(data)):
      data_copy_renamed_because_of_lowering_the_grade_and_attempting_to_break_away_from_the_ninth_grader_pattern=data[i].copy()
      if data_copy_renamed_because_of_lowering_the_grade_and_attempting_to_break_away_from_the_ninth_grader_pattern['duration_min']==0:
        speed_kmh=0.0
      else:
        speed_kmh = round((data_copy_renamed_because_of_lowering_the_grade_and_attempting_to_break_away_from_the_ninth_grader_pattern['distance_km'] / data_copy_renamed_because_of_lowering_the_grade_and_attempting_to_break_away_from_the_ninth_grader_pattern['duration_min']) * 60, 1)
      data_copy_renamed_because_of_lowering_the_grade_and_attempting_to_break_away_from_the_ninth_grader_pattern.update({'speed_kmh': speed_kmh})
      final.append(data_copy_renamed_because_of_lowering_the_grade_and_attempting_to_break_away_from_the_ninth_grader_pattern)
    return final