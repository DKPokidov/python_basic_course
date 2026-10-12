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

code = input()
spec = '@#$%^&*'
have_upper = any(filter(lambda x: x.isalpha() and x.isupper(), code))
have_lower = any(filter(lambda x: x.isalpha() and x.islower(), code))
have_digit = any(filter(lambda x: x.isdigit(), code))
have_one_sym = sum(map(lambda x: code.count(x), spec)) == 1
not_f_or_l = code[0] not in spec and code[-1] not in spec
print(len(code) == 8 and have_upper and have_lower and have_digit and have_one_sym and not_f_or_l)
