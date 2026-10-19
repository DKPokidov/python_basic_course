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

from re import findall
testable = input()
first_condition = bool(findall("[A-Z]+", testable))
second_condition = bool(findall("[a-z]+", testable))
third_condition = bool(findall("[0-9]+", testable))
fourth_condition = findall("[#@#$%^&*]+", testable)
fourth_condition = bool(fourth_condition) and (len(max(fourth_condition, key=len)) == 1) and (len(fourth_condition) == 1)
print((len(testable) == 8) and first_condition and second_condition and third_condition and fourth_condition and (testable[0] not in "#@#$%^&*") and (testable[-1] not in "#@#$%^&*"))