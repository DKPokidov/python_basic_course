"""
Задание 9: Проверка корректности адреса

Адрес считается корректным, если:

* номер дома — целое положительное число;
* название улицы не содержит цифр;
* индекс (в виде строки) состоит ровно из 6 цифр.

Проверьте данные и верните сообщение о правильности или неправильности адреса в зависимости от них.
"""

number_of_the_house = input()
name_of_the_street = input()
indexx = input()

house_ok = number_of_the_house.isdecimal() and int(number_of_the_house) > 0
street_ok = not any(ch.isdigit() for ch in name_of_the_street)
index_ok = indexx.isdecimal() and len(indexx) == 6

if house_ok and street_ok and index_ok:
    print(True)
else:
    print(False)
