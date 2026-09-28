"""
Задание 9: Проверка корректности адреса

Адрес считается корректным, если:

* номер дома — целое положительное число;
* название улицы не содержит цифр;
* индекс (в виде строки) состоит ровно из 6 цифр.

Проверьте данные и верните сообщение о правильности или неправильности адреса в зависимости от них.
"""

adress = (float(input("Введите номер дома: ")), input("Введите название улицы: "), input("Введите индекс: "))

if adress[0] < 0 or not (adress[0].is_integer()):
    print(False)
    quit
elif not adress[1].isalpha():
    print(False)
    quit
elif not adress[2].isnumeric or len(adress[2]) != 6:
    print(False)
    quit
else:
    print(True)
