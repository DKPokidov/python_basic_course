"""
Задание 9: Проверка корректности адреса

Адрес считается корректным, если:

* номер дома — целое положительное число;
* название улицы не содержит цифр;
* индекс (в виде строки) состоит ровно из 6 цифр.

Проверьте данные и верните сообщение о правильности или неправильности адреса в зависимости от них.
"""

# НАПИШИТЕ ВАШ КОД ЗДЕСЬ
# 02_python_structures/practice/01_structures_tasks/task9_address_check.py

house_number = input('Введите номер дома')
street_name = input('Введите название улицы')
postal_code = input('Введите почтовый индекс')

# Проверка: номер дома > 0
valid_house = house_number.isdigit() and int(float(house_number)) > 0

# Проверка: в названии улицы нет цифр
valid_street = street_name.replace(' ', '').isalpha()

# Проверка: индекс — 6 цифр
valid_postal = len(postal_code) == 6 and postal_code.isdigit()

# Итоговый результат
is_address_valid = valid_house and valid_street and valid_postal
print(is_address_valid)
