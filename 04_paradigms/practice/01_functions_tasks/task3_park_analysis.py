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


def _analyze_park(data, threshold=50):

  _density = round(
      data.get('visitors_day') / data.get('area_ha') if data.get('visitors_day') != None and data.get('area_ha') != None else 0, 1
    )

  _entranceLoad = round(
      data.get('visitors_day') / data.get('entrances') if data.get('visitors_day') != None and data.get('entrances') != None else 0
    )
  
  return {

    'density': _density,
    'entrance_load': _entranceLoad,
    'status': 'перегружен' if _density >= threshold else 'в норме',

  } 



def analyze_park(data, threshold=50):

  return {each[0]:_analyze_park(each[1], threshold) for each in data.items()}