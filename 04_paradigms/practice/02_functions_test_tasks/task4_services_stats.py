"""
Задание 4: Статистика по услугам

Аналитический отдел мэрии готовит справочник для жителей: какие услуги
вообще оказываются в городе. Нужно по каждому типу объектов собрать список
услуг, которые там предоставляют, — без дубликатов.

Функция services_stats(data) собирает все уникальные услуги по типам
объектов и возвращает словарь {тип: [список_услуг]}. Услуга учитывается
один раз, даже если встречается у нескольких объектов.

Структура входных данных data:

    {"city": str, "year": int, "objects": [объекты]}

Каждый объект — словарь с полями "type", "name", "district", "capacity",
"coordinates", "accessibility", "services". Услуги объекта — список строк
в поле "services".
"""


def services_stats(data):
    types = []
    for dict_ in data['objects']:
        if dict_['type'] not in types:
            types.append(dict_['type'])
    all_services = [[] for i in range(len(types))]
    for dict_ in data['objects']:
        all_services[types.index(dict_['type'])].extend(dict_['services'])
    for list_ in all_services:
        list_ = set(list_)
        list_ = list(list_)
    return dict(zip(types, all_services))
 

 
        

    