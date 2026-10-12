"""
Задание 9: Проверка корректности адреса

Адрес считается корректным, если:

* номер дома — целое положительное число;
* название улицы не содержит цифр;
* индекс (в виде строки) состоит ровно из 6 цифр.

Проверьте данные и верните сообщение о правильности или неправильности адреса в зависимости от них.
"""

number = int(input('Введите номер дома: '))
name = input("Введите название улицы: ")
ind = input('Введите индекс: ')


has_digit_in_street = any(i.isdigit() for i in name)

is_postal_ok = len(ind) == 6 and ind.isdigit()

is_house_ok = number > 0

is_valid = is_house_ok and not has_digit_in_street and is_postal_ok

print(str(is_valid))