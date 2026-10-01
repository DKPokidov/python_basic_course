"""
Задание 9: Проверка корректности адреса

Адрес считается корректным, если:

* номер дома — целое положительное число;
* название улицы не содержит цифр;
* индекс (в виде строки) состоит ровно из 6 цифр.

Проверьте данные и верните сообщение о правильности или неправильности адреса в зависимости от них.
"""

number_of_house, street, house_index = input(), input(), input()
if "." not in number_of_house and int(number_of_house) > 0:
    m = [i for i in "0123456789" if i in street]
    if len(m) == 0 and len(house_index) == 6:
        print("True")
    else:
        print("False")
else:
    print(False)
