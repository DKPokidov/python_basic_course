# tests/conftest.py
"""
Общие утилиты для всех тестов.
"""

import sys
import io
from unittest.mock import patch
import os

def run_student_code(student_file, inputs):
    """
    Запускает код студента с подставленными input().
    Возвращает всё, что было выведено через print().
    """
    with patch('builtins.input', side_effect=inputs):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        try:
            with open(student_file, 'r', encoding='utf-8') as f:
                code = f.read()
                exec(code)
        except Exception as e:
            sys.stdout = sys.__stdout__
            raise e
        
        sys.stdout = sys.__stdout__
        return captured_output.getvalue().strip()

def get_student_file(module_name, filename):
    """
    Возвращает полный путь к файлу студента.
    
    Args:
        module_name (str): 'module_01' или 'module_02'
        filename (str): Имя файла (например, 'task1_survey.py')
    
    Returns:
        str: Полный путь к файлу
    """
    base_dir = os.path.dirname(os.path.dirname(__file__))
    
    if module_name == 'module_01':
        return os.path.join(base_dir, '01_python_basics', 'practice', '01_intro_tasks', filename)
    elif module_name == 'module_02':
        return os.path.join(base_dir, '01_python_basics', 'practice', '02_intro_tasks', filename)
    elif module_name == 'module_03':
        return os.path.join(base_dir, '02_python_structures', 'practice', '01_structures_tasks', filename)
    else:
        return os.path.join(base_dir, module_name, 'practice', filename)