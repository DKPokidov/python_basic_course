#!/usr/bin/env python3
"""
Локальный валидатор для проверки заданий перед пушем.
Запуск: python utils/validator.py
"""

import os
import sys
import importlib

# Список тем и соответствующих файлов для проверки
TOPICS = {
    'topic_01_python_basics': {
        'files': ['task1_variables.py', 'task2_conditions.py', 'task3_loops.py', 'task4_functions.py'],
        'functions': [
            ('task1_variables', 'create_variables'),
            ('task1_variables', 'calculate_age'),
            ('task1_variables', 'string_concatenation'),
            ('task2_conditions', 'check_age'),
            ('task2_conditions', 'compare_numbers'),
            ('task3_loops', 'sum_numbers'),
            ('task3_loops', 'find_max'),
            ('task4_functions', 'greet_user'),
            ('task4_functions', 'power_of_two'),
        ]
    },
    'topic_02_data_structures': {
        'files': ['task1_list_operations.py', 'task2_dict_operations.py', 'task3_comprehensions.py'],
        'functions': [
            ('task1_list_operations', 'reverse_list'),
            ('task1_list_operations', 'find_duplicates'),
            ('task2_dict_operations', 'merge_dicts'),
            ('task2_dict_operations', 'invert_dict'),
            ('task3_comprehensions', 'square_numbers'),
            ('task3_comprehensions', 'filter_even'),
        ]
    },
    # Добавьте остальные темы по аналогии
}

def check_file_exists(topic_path, filename):
    """Проверяет существование файла"""
    full_path = os.path.join(topic_path, filename)
    if not os.path.exists(full_path):
        print(f"❌ Файл {filename} не найден в {topic_path}")
        return False
    print(f"✅ Файл {filename} найден")
    return True

def check_function_exists(module_name, function_name, topic_path):
    """Проверяет наличие функции в модуле"""
    try:
        sys.path.insert(0, topic_path)
        module = importlib.import_module(module_name)
        if hasattr(module, function_name):
            print(f"✅ Функция {function_name} найдена в {module_name}")
            return True
        else:
            print(f"❌ Функция {function_name} не найдена в {module_name}")
            return False
    except ImportError:
        print(f"❌ Модуль {module_name} не найден в {topic_path}")
        return False
    finally:
        sys.path.pop(0)

def validate_all():
    """Запускает все проверки"""
    print("=" * 60)
    print("🔍 Проверка заданий перед отправкой")
    print("=" * 60)
    
    errors = 0
    
    for topic, config in TOPICS.items():
        print(f"\n📁 {topic.replace('_', ' ').title()}")
        topic_path = os.path.join(topic, 'practice')
        
        # Проверяем файлы
        for file in config['files']:
            if not check_file_exists(topic_path, file):
                errors += 1
        
        # Проверяем функции
        for module_name, func_name in config['functions']:
            if not check_function_exists(module_name, func_name, topic_path):
                errors += 1
    
    # Итог
    print("\n" + "=" * 60)
    if errors == 0:
        print("🎉 ВСЕ ПРОВЕРКИ ПРОЙДЕНЫ! Можно пушить.")
    else:
        print(f"❌ Найдено {errors} ошибок. Исправьте перед пушем.")
    print("=" * 60)
    
    return errors == 0

if __name__ == "__main__":
    sys.exit(0 if validate_all() else 1)