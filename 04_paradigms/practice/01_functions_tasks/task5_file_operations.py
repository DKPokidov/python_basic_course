"""
Задание 5: Работа с файлами

Системный администратор городского архива хочет автоматизировать обычную
процедуру: файл-источник перенести в архивную зону под новым именем,
а оригинал удалить, чтобы на диске не плодились дубликаты. Раньше это
делали вручную — теперь поручают скрипту.

Напишите скрипт, который в текущей директории:

1. Создаёт файл original.txt и записывает в него строку «Это оригинальный файл.».
2. Копирует original.txt в copy.txt.
3. Переименовывает copy.txt в renamed_copy.txt.
4. Удаляет original.txt.

В конце работы должен существовать только файл renamed_copy.txt
с сохранённым содержимым, а файлы original.txt и copy.txt не должны
существовать.
"""

import os


with open('original.txt', 'w+', encoding='utf-8') as original:
    original.write("Это оригинальный файл.")
with open('copy.txt', 'w+', encoding='utf-8') as copy:
    text = []
    with open('original.txt', 'r', encoding='utf-8') as original:
        text.extend(original.readlines())
    copy.writelines(text)
if os.path.exists('copy.txt'):
    os.rename('copy.txt', 'renamed_copy.txt')
if os.path.exists('original.txt'):
    os.remove('original.txt')
