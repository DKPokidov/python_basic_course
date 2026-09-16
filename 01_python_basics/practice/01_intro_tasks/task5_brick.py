# module_01_python_basics/practice/task5_geometry.py
"""
Задание 5: Кирпич

Напишите программу, которая:
1. Запрашивает длину кирпича (см)
2. Запрашивает ширину кирпича (см)
3. Запрашивает высоту кирпича (см)
4. Вычисляет и выводит:
   - Объём (см³): длина * ширина * высота
   - Площадь поверхности (см²): 2 * (д*ш + ш*в + д*в)
   - Сумму рёбер (см): 4 * (д + ш + в)
   - Массу (кг): объём(м³) * 1700
   - Количество кирпичей в 1 м³

Примечание: все числовые значения — дробные (float).
Для ввода используйте float(input()), а не int(input()).

Пример:
Введите длину кирпича (см): 25.0
Введите ширину кирпича (см): 12.0
Введите высоту кирпича (см): 6.5
Объём: 1950.0 см³
Площадь поверхности: 1081.0 см²
Сумма рёбер: 174.0 см
Масса: 3.31 кг
Количество кирпичей в 1 м³: 512
"""

print("Введите длину кирпича (см): ")
length = float(input())
print("Введите ширину кирпича (см): ")
width = float(input())
print("Введите высоту кирпича (см): ")
height = float(input())
volume = length * width * height
surface_area = 2 * (length * width + width * height + length * height)
edge_sum = 4 * (length + width + height)
# Convert volume from cm³ to m³ for mass calculation
volume_m3 = volume / 1_000_000  # 1 m³ = 1,000,000 cm³
mass = volume_m3 * 1700  # Density of brick is 1700 kg/m³
bricks_per_m3 = int(1_000_000 / volume)  # Number of bricks in 1 m³
print(f"Объём: {volume} см³")
print(f"Площадь поверхности: {surface_area} см²")
print(f"Сумма рёбер: {edge_sum} см")
print(f"Масса: {mass:.2f} кг")
print(f"Количество кирпичей в 1 м³: {bricks_per_m3}")
