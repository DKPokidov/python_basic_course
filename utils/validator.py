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
        "practice/01_structures_tasks": [
            "task1_benches.py",
            "task2_finds.py",
            "task3_coffee_shops.py",
            "task4_expenses.py",
            "task5_slogan.py",
            "task6_scholarships.py",
            "task7_truth_tables.py",
            "task8_street_name.py",
            "task9_address_check.py",
            "task10_pirate_ship.py",
            "task11_chessboard_white.py",
            "task12_chessboard_same_color.py",
            "task13_buildings.py",
            "task14_secret_code.py",
            "task15_apartment.py",
        ],
    },
    "03_control_flow": {
        "practice/01_control_flow_tasks": [
            "task1_building_category.py",
            "task2_floors_limit.py",
            "task3_green_zones.py",
            "task4_attractions.py",
            "task5_routes.py",
            "task6_streets.py",
            "task7_green_areas.py",
            "task8_dense_districts.py",
            "task9_green_balance.py",
            "task10_city_growth.py",
        ],
        "practice/02_control_flow_tasks": [
            "task11_routes.py",
            "task12_streets.py",
            "task13_green_areas.py",
            "task14_dense_districts.py",
            "task15_green_balance.py",
            "task16_city_growth.py",
            "task17_stop_load.py",
            "task18_quarters.py",
        ],
    },
    "04_paradigms": {
        "practice/01_functions_tasks": [
            "task1_analyze_grades.py",
            "task2_bus_routes.py",
            "task3_park_analysis.py",
            "task4_scooter_usage.py",
            "task5_file_operations.py",
            "task6_parking_analysis.py",
        ],
        "practice/02_functions_test_tasks": [
            "task1_filter_by_type.py",
            "task2_accessibility_analysis.py",
            "task3_find_overloaded.py",
            "task4_services_stats.py",
            "task5_geospatial.py",
        ],
        "practice/03_OOP_tasks": [
            "task1_city_district.py",
            "task2_building.py",
            "task3_district.py",
            "task4_building_types.py",
            "task5_university.py",
            "task6_vehicles.py",
        ],
        "practice/04_iterator_generator_tasks": [
            "task1_count_up_to.py",
            "task2_greetings.py",
            "task3_prime_iterator.py",
            "task4_noisy_measurements.py",
        ],
    },
    "05_api": {
        "practice/01_api_tasks": [
            "task1_fetch_rates.py",
            "task2_parse_currency.py",
            "task3_currency_report.py",
            "task4_savings.py",
        ],
    },
    "06_test assignment": {
        ".": ["Final_labaratory_work.ipynb"],
    },
    "07_data_analysis": {
        "practice": [
            "01_numpy_practice_gdz.ipynb",
            "02_Pandas_practice.ipynb",
            "03_analysis_task.ipynb",
            "04_geopandas_osmnx_practice.ipynb",
            "05_titanic_exam.ipynb",
        ],
    },
    "08_geoanalysis": {
        "Practice": ["04_okn_analysis.ipynb"],
    },
    "09_visualization": {
        "practice": [
            "01_visualization_practice.ipynb",
            "02_titanic_visulization.ipynb",
        ],
    },
    "10_final_project": {
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
