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
password = input ('Введите код доступа:')
cond1 = len(password) == 8

cond2 = any(char.isupper() for char in password)

cond3 = any(char.islower() for char in password)

cond4 = any(char.isdigit() for char in password)

special_chars = "#@#$%^&*"
cond5 = sum(1 for char in password if char in special_chars) == 1

cond6 = (password[0] not in special_chars) and (password[-1] not in special_chars)

result = cond1 and cond2 and cond3 and cond4 and cond5 and cond6

print(result)
