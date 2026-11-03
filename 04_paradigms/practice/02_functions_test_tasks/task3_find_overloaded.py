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

    pairsSatisfying: list[tuple[str, int]] = list(
        map(
            (lambda _obj: (_obj['name'], _obj['capacity'])),
            filter(
                (lambda _obj: _obj['capacity'] > threshold),
                data['objects']
            )
        )
    )

    return list(
        map(
            (lambda pair: f"{pair[0]} ({pair[1]} мест)"),
            pairsSatisfying
        )
    )
