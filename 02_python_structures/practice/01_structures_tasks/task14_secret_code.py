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
code_symbols = []
code_symbols.extend(input())
list_bul = []
list_ABC = []
list_abc = []
list_digits = []
list_special = []
list_ABC.extend("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
list_abc.extend("ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower())
list_digits.extend('1234567890')
list_special.extend('#@#$%^&*')
list_bul.append(len(code_symbols) == 8)
list_bul.append(len(set(code_symbols).intersection(set(list_ABC))) > 0)
list_bul.append(len(set(code_symbols).intersection(set(list_abc))) > 0)
list_bul.append(len(set(code_symbols).intersection(set(list_digits))) > 0)
list_bul.append(len(set(code_symbols).intersection(set(list_special))) == 1)
list_bul.append(code_symbols[0] not in '#@#$%^&*' and code_symbols[-1] not in '#@#$%^&*')
print(list_bul[0] * list_bul[1] * list_bul[2] * list_bul[3] * list_bul[4] * list_bul[5] == 1)