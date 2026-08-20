"""
Задание 5: Работа с файлами

Скрипт создаёт файл original.txt, записывает в него строку,
копирует его в copy.txt, переименовывает копию в renamed_copy.txt,
удаляет original.txt.
"""

# НАПИШИТЕ ВАШ КОД ЗДЕСЬ
# 04_paradigms/practice/01_functions_tasks/task5_file_operations.py

import os
import shutil

file_path = 'original.txt'
with open(file_path, 'w') as f:
    f.write("Это оригинальный файл.\n")

if os.path.exists(file_path):
    print("Файл успешно создан:", file_path)

shutil.copy(file_path, 'copy.txt')
print("Файл скопирован как copy.txt")

os.rename('copy.txt', 'renamed_copy.txt')
print("Файл переименован в renamed_copy.txt")

os.remove(file_path)
print("Оригинальный файл удалён")

if os.path.exists('renamed_copy.txt'):
    print("Копия файла существует!")
