"""
Задание 9: Проверка корректности адреса

Адрес считается корректным, если:

* номер дома — целое положительное число;
* название улицы не содержит цифр;
* индекс (в виде строки) состоит ровно из 6 цифр.

Проверьте данные и верните сообщение о правильности или неправильности адреса в зависимости от них.
"""
number = input('Введите номер дома ')
name = input('Введите название улицы ')
indeks = input('Введите индекс ')
okeynumber = len(number) > 0 and number.isdigit() and int(number) > 0
okeyname = name.replace(" ", "").isalpha() and len(name) > 0
okeyindeks = len(indeks) == 6 and indeks.isdigit()
print(okeyindeks and okeynumber and okeyname)