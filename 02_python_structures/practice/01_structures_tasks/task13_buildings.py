"""
Задание 13: Анализ списка зданий

Есть список зданий (кортеж словарей).

Нужно одним выражением (без циклов и if) получить список id зданий, которые:

* имеют площадь >= 1000 кв. метров И
* не менее 4 этажей И
* тип — «жилой».

Списки зданий уже заданы. Выведите полученный список id, например: [1, 4]
"""

buildings = (
    {"id": 1, "площадь": 1200, "этажи": 6, "тип": "жилой"},
    {"id": 2, "площадь": 800, "этажи": 3, "тип": "жилой"},
    {"id": 3, "площадь": 1500, "этажи": 5, "тип": "офис"},
    {"id": 4, "площадь": 1000, "этажи": 4, "тип": "жилой"},
    {"id": 5, "площадь": 900, "этажи": 5, "тип": "жилой"},
)
list_bul = []
list_bul.append(buildings[0]['площадь'] >= 1000 and buildings[0]['этажи'] >= 4 and buildings[0]['тип'] == 'жилой')
list_bul.append(buildings[1]['площадь'] >= 1000 and buildings[1]['этажи'] >= 4 and buildings[1]['тип'] == 'жилой')
list_bul.append(buildings[2]['площадь'] >= 1000 and buildings[2]['этажи'] >= 4 and buildings[2]['тип'] == 'жилой')
list_bul.append(buildings[3]['площадь'] >= 1000 and buildings[3]['этажи'] >= 4 and buildings[3]['тип'] == 'жилой')
list_bul.append(buildings[4]['площадь'] >= 1000 and buildings[4]['этажи'] >= 4 and buildings[4]['тип'] == 'жилой')
string_find = str(list_bul[0])[0] + str(list_bul[1])[0] + str(list_bul[2])[0] + str(list_bul[3])[0] + str(list_bul[4])[0]
index_find = []
index_find.append(string_find.find('T') + 1)
index_find.append(string_find.rfind('T') + 1)
print(index_find)