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


alphabet_low = 'abcdefghijklmnopqrstuvwxyz'
alphabet_high = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet_num = '0123456789'
alphabet_special = '#@#$%^&*'

def intersect_str(str1: str, str2: str) -> set[str]:
    return set(str1) & set(str2)

def check_string(x: str) -> bool:
    return (
        len(intersect_str(x, alphabet_high)) >= 1 and
        len(intersect_str(x, alphabet_low)) >= 1 and
        len(intersect_str(x, alphabet_num)) >= 1 and
        len(intersect_str(x, alphabet_special)) == 1 and
        len(intersect_str(x[0] + x[len(x) - 1], alphabet_special)) == 0 and
        len(x) == 8
    )

print(check_string(input()))