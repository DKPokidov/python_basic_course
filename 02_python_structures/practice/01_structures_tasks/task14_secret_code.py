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
import string
code = input()
special = '#@#$%^&*'
chars = set(code)
len_ok = len(code) == 8
upper_ok = bool(chars & set(string.ascii_uppercase))
lower_ok = bool(chars & set(string.ascii_lowercase))
digit_ok = bool(chars & set(string.digits))
spec_count = (code.count('#') + code.count('@') + code.count('$') +
              code.count('%') + code.count('^') + code.count('&') +
              code.count('*'))
spec_first_last = False
if code[0] not in '#@#$%^&*' and code[-1] not in '#@#$%^&*':
    spec_first_last = True

is_valid = len_ok and upper_ok and lower_ok and digit_ok and spec_first_last and spec_count == 1

print(is_valid)
