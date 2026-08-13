#!/usr/bin/env python3
"""
Локальный валидатор для проверки заданий перед пушем.
Запуск: python utils/validator.py
"""

import os
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

# Ожидаемые файлы курса по модулям (пути относительно корня репозитория)
MODULES = {
    "01_python_basics": {
        "practice/01_intro_tasks": [
            "task1_survey.py",
            "task2_park_area.py",
            "task3_coins.py",
            "task4_weight_converter.py",
            "task5_brick.py",
            "task6_call_duration.py",
            "task7_wifi_password.py",
            "task8_bench_timer.py",
            "task9_time_diff.py",
        ],
        "practice/02_intro_tasks": [
            "task10_visiting_card.py",
            "task11_cryo_age.py",
            "task12_email_generator.py",
            "task13_story_maker.py",
            "task14_formula.py",
            "task15_jumpers.py",
        ],
    },
    "02_python_structures": {
        "practice": ["01_practice_structures_gdz.ipynb"],
    },
    "03_control_flow": {
        "practice": [
            "01_practice_control_flow_gdz.ipynb",
            "02_practice_control_flow_gdz.ipynb",
        ],
    },
    "04_paradigms": {
        "practice": [
            "01_practice_functions_gdz.ipynb",
            "02_practice_functions_test_gdz_.ipynb",
            "03_practice_OOP_gdz.ipynb",
            "04_practice_itarator&generator_gdz.ipynb",
        ],
    },
    "05_api_osm": {
        "practice": ["01_API&osmnx_gdz.ipynb"],
    },
    "06_data_analysis": {
        "practice": [
            "01_numpy_practice_gdz.ipynb",
            "02_Pandas_practice.ipynb",
            "03_analysis_task.ipynb",
            "04_geopandas_osmnx_practice.ipynb",
            "05_titanic_exam.ipynb",
        ],
    },
    "07_visualization": {
        "practice": [
            "01_visualization_practice.ipynb",
            "02_titanic_visulization.ipynb",
        ],
    },
    "08_final_project": {
        ".": ["01_covid_analysis.ipynb"],
    },
}


def check_file_exists(filepath):
    """Проверяет существование файла"""
    if os.path.exists(filepath):
        print(f"✅ {filepath}")
        return True
    print(f"❌ {filepath} не найден")
    return False


def validate_all():
    """Запускает все проверки"""
    print("=" * 60)
    print("🔍 Проверка заданий перед отправкой")
    print("=" * 60)

    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    errors = 0

    for module, subdirs in MODULES.items():
        print(f"\n📁 {module}")
        for subdir, files in subdirs.items():
            for filename in files:
                full_path = os.path.join(root, module, subdir, filename)
                if not check_file_exists(full_path):
                    errors += 1

    print("\n" + "=" * 60)
    if errors == 0:
        print("🎉 ВСЕ ПРОВЕРКИ ПРОЙДЕНЫ! Можно пушить.")
    else:
        print(f"❌ Найдено {errors} ошибок. Исправьте перед пушем.")
    print("=" * 60)

    return errors == 0


if __name__ == "__main__":
    sys.exit(0 if validate_all() else 1)
