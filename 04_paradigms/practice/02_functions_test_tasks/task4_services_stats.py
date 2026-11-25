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
    result = {}

    for object in data['objects']:
        if object['type'] not in result:
            services_list = []
            for service in object['services']:
                if service not in services_list:
                    services_list.append(service)
            result[object['type']] = services_list
        else:
            for service in object['services']:
                if service not in result[object['type']]:
                    result[object['type']].append(service)
    return result
