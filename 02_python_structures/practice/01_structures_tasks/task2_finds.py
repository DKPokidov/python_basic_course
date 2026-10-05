"""
Задание 2: Поиск потерянных наушников

В кампусе ИТМО постоянно теряют наушники. Создайте систему для отслеживания находок!
Данные о находках за два дня уже заданы.

Пример вывода:
1. Находили оба дня: {'беспроводные Sony'}
2. Только сегодня: {'Samsung Buds', 'старые советские'}
3. Всего уникальных моделей: 5
"""

yesterday = {"беспроводные Sony", "AirPods", "JBL"}
today = {"беспроводные Sony", "Samsung Buds", "старые советские"}

import datetime

# сформируем нормальную систему. для этого воспользуемся двумя связанными структурами:

# parentdict сохраняет все подсловари и обладает первой записью nextId, которая позволяет каждому новому предмету получить уникальный идентификатор
# крч проще говоря считает все записи

parentdict_ = {
    'nextId': 0
}


# добавляет предмет в parentdict

def create_find(parentdict: dict, model: str, date: datetime.date, id=None) -> dict: 

    parentdict['nextId'] += 1  

    itemId = parentdict['nextId'] if (id == None) or (id in list(map(lambda x: x['id']), parentdict)) else id
    item = {
        'model': model,
        'date': date,
        'parentdict' : parentdict,
        'id': itemId
    }

    parentdict[itemId] = item
    return item

create_find(parentdict_, 'старые советские', datetime.date.today())
create_find(parentdict_, 'Samsung Buds', datetime.date.today())
create_find(parentdict_, 'беспроводные Sony', datetime.date.today())
create_find(parentdict_, 'JBL', datetime.date.fromisocalendar(
    datetime.date.today().isocalendar().year,
    datetime.date.today().isocalendar().week,
    datetime.date.today().isocalendar().weekday + 1 )
)
create_find(parentdict_, 'AirPods', datetime.date.fromisocalendar(
    datetime.date.today().isocalendar().year,
    datetime.date.today().isocalendar().week,
    datetime.date.today().isocalendar().weekday + 1 )
)
create_find(parentdict_, 'беспроводные Sony', datetime.date.fromisocalendar(
    datetime.date.today().isocalendar().year,
    datetime.date.today().isocalendar().week,
    datetime.date.today().isocalendar().weekday + 1 )
)







# сделаем функции для анализа 

def unique_all(parentdict: dict) -> set[str]:

    unique_models = set()
    for each in parentdict.values():
        if type(each) != int:
            unique_models.add(each['model'])

    return unique_models

def bothdays(parentdict: dict):

    date_today = datetime.date.today()
    date_yesterday = datetime.date.fromisocalendar(
        date_today.isocalendar().year,
        date_today.isocalendar().week,
        (date_today.isocalendar().weekday + 1) # по хорошему, у викдей проперти есть геттер который меняет и неделю, и год, если нужно
    )

    dict_both: dict[list] = {
        
    }
    final_models = []


    for each in parentdict.values():
        if type(each) != int:
            if each['date'] == date_today or each['date'] == date_yesterday:
                try:
                    dict_both[each['model']] += [each['id']]
                except KeyError:
                    dict_both[each['model']] = [each['id']]

    for each2 in dict_both.values():

        if type(each2) != int:

            if len(each2) > 1:
                dateset = set()
                for ids in each2:
                    dateset.add(parentdict[ids]['date'].isocalendar())
                if len(dateset) > 1:
                    final_models.append(parentdict[ids]['model'])


    return final_models
                

    


def unique_daily(parentdict: dict):

    dict_bymodel = {}
    fin_models = []

    for each in parentdict.values():
        if type(each) != int:
            try:
                dict_bymodel[each['model']] += [each['id']]
            except KeyError:
                dict_bymodel[each['model']] = [each['id']]

    for each in dict_bymodel.values():
            if type(each) != int:
                if len(set(map(lambda x: parentdict[x]['date'], each))) == 1 and parentdict[each[0]]['date'] == datetime.date.today():
                    fin_models.append(parentdict[each[0]]['model'])
    

    return fin_models

    

print(f"Находили оба дня: {set(bothdays(parentdict_))}")
print(f"Только сегодня: {set(unique_daily(parentdict_))}")
print(f"Всего уникальных моделей: {len(unique_all(parentdict_))}")