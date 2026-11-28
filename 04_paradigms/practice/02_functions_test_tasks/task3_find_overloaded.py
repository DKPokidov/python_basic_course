"""
Задание 3: Поиск перегруженных объектов

Школьные столовые, спортзалы и библиотеки города жалуются на переполнение.
Департамент решил выделить субсидии объектам, чья вместимость превышает
норму, — им нужно срочно расширяться. Помогите департаменту найти такие
объекты в базе.

Функция find_overloaded(data, threshold) находит объекты, где
capacity > threshold. Возвращает список строк "{name} ({capacity} мест)".

Структура входных данных data:

    {"city": str, "year": int, "objects": [объекты]}

Каждый объект — словарь с полями "type", "name", "district", "capacity",
"coordinates", "accessibility", "services".

Строки возвращаются в порядке следования объектов в данных.
"""


def find_overloaded(data, threshold):
    names = [dict_['name'] for dict_ in data['objects'] if dict_['capacity'] > threshold]
    capacitys = [dict_['capacity'] for dict_ in data['objects'] if dict_['capacity'] > threshold]
    #for dict_ in data['objects']:
    #   if dict_['capacity'] > threshold:
    #       names.append(dict_['name'])
    #      capacitys.append(dict_['capacity'])
    return [f'{names[i]} ({capacitys[i]} мест)' for i in range(len(names))]
    #for i in range(len(names)):
    #    answer.append(f'{names[i]} ({capacitys[i]} мест)')
    # return answer

