"""
Задание 2: Оптимизация автобусных маршрутов

Написать функции:
1. load_per_km(route) — загруженность (пас./км), round до 1 знака.
   Вход: dict {"number": int, "length": float, "passengers": int}
2. needs_review(load) — True если загруженность < 200
"""

# НАПИШИТЕ ВАШ КОД ЗДЕСЬ
# 04_paradigms/practice/01_functions_tasks/task2_bus_routes.py


def load_per_km(route):
    return round(route["passengers"] / route["length"], 1)


def needs_review(load):
    return load < 200
