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
    keys_list = []
    value_list = []
    for name, info in data.items():
        density = round(info['visitors_day'] / info['area_ha'], 1)
        entrance_load = round(info['visitors_day'] / info['entrances'])
        stat = lambda x: 'перегружен' if x >= threshold else 'в норме'
        status = stat(density)
        keys_list.append(name)
        value_list.append({'density' : round(density, 1), 'entrance_load' : entrance_load, 'status' : status})
    return dict(zip(keys_list, value_list))

print(analyze_park( {"Парк Победы": {"visitors_day": 6000, "area_ha": 100, "entrances": 4}}))