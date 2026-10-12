"""
Задание 9: Проверка корректности адреса

Адрес считается корректным, если:

* номер дома — целое положительное число;
* название улицы не содержит цифр;
* индекс (в виде строки) состоит ровно из 6 цифр.

Проверьте данные и верните сообщение о правильности или неправильности адреса в зависимости от них.
"""
house_number = input('Введите номер вашего дома: ')
street = input('Введите вашу улицу: ')
house_index = input('Введите ваш индекс: ')

is_house_number_ok = (house_number.isdigit() and int(house_number) > 0)
is_street_ok = (not any(c.isdigit() for c in street) and len(street) > 0)
is_house_index_ok = (len(house_index) == 6 and house_index.isdigit())

is_adress_ok = ['адрес неправильный', 'адрес правильный']
checking = int(is_house_number_ok and is_street_ok and is_house_index_ok)
print(is_adress_ok[checking])
