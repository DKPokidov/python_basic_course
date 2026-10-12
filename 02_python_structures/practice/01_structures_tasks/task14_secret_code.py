"""
Задание 14: Секретный код доступа

Вы — агент спецслужбы. Вам передали зашифрованное сообщение с кодом доступа к серверу.
Код должен соответствовать строгим правилам безопасности. Ваша задача — проверить,
является ли предоставленная строка валидным кодом доступа, не используя циклы и условные операторы.

Код считается корректным, если:
* длина строки — ровно 8 символов;
* содержит хотя бы одну заглавную букву (A-Z);
* содержит хотя бы одну строчную букву (a-z);
* включает хотя бы одну цифру (0-9);
* имеет ровно один специальный символ из набора: #@#$%^&*;
* специальный символ не может стоять на первой или последней позиции.
"""
password = input("Введите код доступа: ")
str_length = len(password) == 8
odn_zaglav = any(char.isupper() for char in password)
odn_strochn = any(char.islower() for char in password)
odn_cifra = any(char.isdigit() for char in password)
special_chars = set("#@#$%^&*")
special_not_first = password[0] not in special_chars and password[-1] not in special_chars

if str_length and odn_zaglav and odn_strochn and odn_cifra and special_not_first:
    print("Код доступа корректен")
else:
    print("Код доступа некорректен")