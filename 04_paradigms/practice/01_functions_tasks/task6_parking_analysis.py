"""
Задание 6: Анализ загруженности городских парковок

Прочитать файл parkings.txt (формат: "название;вместимость;занято" по строкам),
вычислить процент занятости, добавить поле занятость_%, отфильтровать >80%,
записать в high_load_parkings.txt.
"""

# НАПИШИТЕ ВАШ КОД ЗДЕСЬ
# 04_paradigms/practice/01_functions_tasks/task6_parking_analysis.py

with open('../../data/parkings.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

result_lines = []
for i, line in enumerate(lines):
    if i == 0:
        continue
    if line.strip():
        name, capacity, occupied = line.strip().split(';')
        capacity = int(capacity)
        occupied = int(occupied)
        load_percent = round(occupied / capacity * 100, 1)
        new_line = f"{name};{capacity};{occupied};{load_percent}\n"
        if load_percent > 80:
            result_lines.append(new_line)

with open('../../data/high_load_parkings.txt', 'w', encoding='utf-8') as f:
    f.write("название_парковки;вместимость;занято;занятость_%\n")
    f.writelines(result_lines)
