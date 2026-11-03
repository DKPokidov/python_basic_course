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

    returnDict: dict[str, list] = {}

    for dataObject in data['objects']:

        if returnDict.get(dataObject['type']) == None:
            returnDict[dataObject['type']] = []

        returnDict[dataObject['type']] += dataObject['services']


    print(returnDict.items())

    return {key: value for (key, value) in tuple(map(
        (lambda x: (x[0], set(x[1]))),
        returnDict.items()
    ))}
