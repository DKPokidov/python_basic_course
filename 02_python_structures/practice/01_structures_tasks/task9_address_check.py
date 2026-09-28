"""
Задание 9: Проверка корректности адреса

Адрес считается корректным, если:

* номер дома — целое положительное число;
* название улицы не содержит цифр;
* индекс (в виде строки) состоит ровно из 6 цифр.

Проверьте данные и верните сообщение о правильности или неправильности адреса в зависимости от них.
"""

number = input("Номер ")
name = input("Название ")
index = input("Индекс ")

print((int(number) > 0 and float(number) == int(number)) and not any(filter(lambda x: x.isdigit(), name)) and (len(index) == 6 and all(filter(lambda x: x.isdigit(), index))))
