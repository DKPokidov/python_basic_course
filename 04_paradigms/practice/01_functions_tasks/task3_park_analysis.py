"""
Задание 3: Анализ загруженности городских парков

Отдел благоустройства собрал данные по городским паркам: сколько человек
приходит в парк за день, какова его площадь в гектарах и сколько у парка
входов. По этим цифрам нужно понять, какие парки перегружены толпой
и в какие можно смело вкладывать деньги.

Напишите функцию analyze_park(data, threshold=50), где:
- data: dict {название: {"visitors_day": int, "area_ha": int, "entrances": int}}
- Для каждого парка вычисляется:
    density       = round(visitors_day / area_ha, 1)  — посетителей на гектар;
    entrance_load = round(visitors_day / entrances)   — посетителей на один вход.
- Парк считается перегруженным (status = "перегружен"), если
  density >= threshold, иначе — "в норме".
- Функция возвращает dict {название: {"density": ..., "entrance_load": ...,
                                       "status": ...}}.
"""


def analyze_park(data, threshold=50):
    final_data = dict()
    for park, pdata in data:
      density = round(pdata['visitors_day'] / pdata['area_ha'], 1)
      entrance_load = round(pdata['visitors_day'] / pdata['entrances'])
      status = str()
      if density >= threshold:
          status = 'перегружен'
      else:
          status = 'в норме'
      final_data[park] = {'density': density, 'entrance_load': entrance_load, 'status': status}
    return final_data
