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

length_valid = len(password) == 8
uppercase_valid = password.lower() != password
lowercase_valid = password.upper() != password
digit = (password.count("0") + password.count("1") + password.count("2") + password.count("3") + password.count("4") + password.count("5") + password.count("6") + password.count("7") + password.count("8") + password.count("9")) >= 1
simb = password.count("#") + password.count("@") + password.count("$") + password.count("%") + password.count("^") + password.count("&") + password.count("*") == 1
simb_position = (len(password) == 8) and (password[0] not in "#@$%^&*") and (password[-1] not in "#@$%^&*")

print(f"Код доступа валиден: {length_valid and uppercase_valid and lowercase_valid and digit and simb and simb_position}")
