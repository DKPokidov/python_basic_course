"""
Задание 15: Покупка квартиры

Петр Петрович заработал солидную сумму и, боясь инфляции, решил купить квартиру,
которая должна удовлетворять следующим условиям:
* площадь от 120 кв. метров в любом районе или площадь от 70 кв. метров, но в Центральном районе;
* площадь кухни должна быть не меньше 20 кв. метров;
* обязательно наличие балкона.

Напишите программу, которая определяет, соответствует ли квартира данным критериям.

Внимание: использовать IF-ELSE запрещается.

Программа должна выводить сообщение «Квартира подходит» или «Квартира не подходит».
"""

area = int(input())
district = input().strip()
kitchen_area = int(input())
has_balcony_raw = input().strip().lower()
has_balcony = has_balcony_raw == "да"

condition_area = (area >= 120) or (area >= 70 and district == "Центральный")

condition_kitchen = kitchen_area >= 20

#condition_balcony = has_balcony

is_suitable = condition_area and condition_kitchen and has_balcony

messages = ["Квартира не подходит", "Квартира подходит"]
print(messages[int(is_suitable)])
# py -m pytest tests/test_02_python_structures/test_task15_apartment.py -v 