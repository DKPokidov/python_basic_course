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
  keys=[]
  values=[]
  for name, info in data.items():
    density=info['visitors_day']/info['area_ha']
    entrance_load=info['visitors_day']/info['entrances']
    stat=lambda den: 'в норме' if den<threshold else 'перегружен'
    status=stat(density)
    keys.append(name)
    values.append({'density': round(density,1), 'entrance_load': round(entrance_load,0),'status':status})
  return dict(zip(keys,values))