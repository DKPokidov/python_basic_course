"""
Задание 9: Проверка корректности адреса

Адрес считается корректным, если:

* номер дома — целое положительное число;
* название улицы не содержит цифр;
* индекс (в виде строки) состоит ровно из 6 цифр.

Проверьте данные и верните сообщение о правильности или неправильности адреса в зависимости от них.
"""
house = input("Введите номер дома: ")
street = input("Введите название улицы: ")
index = input("Введите индекс: ")

house_ok = house.isdigit() and int(house) > 0

street_ok = True
for symbol in street:
    if symbol.isdigit():
        street_ok = False

index_ok = len(index) == 6 and index.isdigit()


if house_ok and street_ok and index_ok:
    print("Адрес корректный")
else:
    print("Адрес некорректный")