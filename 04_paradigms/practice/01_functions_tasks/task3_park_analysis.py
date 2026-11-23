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


def analyze_park(data, threshold=50) -> dict:
    names = list(map(str, data.keys()))
    print(names)
    result = {name: {} for name in names}
    for name in names:
      cur = data[name]
      visitors_day = cur["visitors_day"]
      area_ha = cur["area_ha"]
      entrances = cur["entrances"]
      density = round(visitors_day / area_ha, 1)
      entrance_load = round(visitors_day / entrances)
      status = ["в норме", "перегружен"][density >= threshold]
      result[name]["density"] = density
      result[name]["entrance_load"] = entrance_load
      result[name]["status"] = status
    return result
    pass

# data_1 = {"Парк А": {"visitors_day": 6000, "area_ha": 50, "entrances": 5}, "Парк Б": {"visitors_day": 1000, "area_ha": 100, "entrances": 2}}
# print(data_1["Парк Б"])
# analyze_park(data_1)