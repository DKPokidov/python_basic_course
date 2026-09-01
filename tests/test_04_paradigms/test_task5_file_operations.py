# tests/test_04_paradigms/test_task5_file_operations.py
"""
Тесты для задания 5: Работа с файлами
"""

import os
from tests.test_04_paradigms.conftest import run_student_code, get_module06_file


class TestTask5FileOperations:
    """Тесты для задания 5: Работа с файлами"""

    student_file = get_module06_file('task5_file_operations.py')

    def test_file_operations(self, monkeypatch, tmp_path):
        monkeypatch.chdir(tmp_path)
        output = run_student_code(self.student_file, [])
        assert "Файл успешно создан: original.txt" in output
        assert "Файл скопирован как copy.txt" in output
        assert "Файл переименован в renamed_copy.txt" in output
        assert "Оригинальный файл удалён" in output
        assert "Копия файла существует!" in output
        assert os.path.exists(os.path.join(tmp_path, "renamed_copy.txt"))
        assert not os.path.exists(os.path.join(tmp_path, "original.txt"))
        assert not os.path.exists(os.path.join(tmp_path, "copy.txt"))

    def test_renamed_copy_content(self, monkeypatch, tmp_path):
        monkeypatch.chdir(tmp_path)
        run_student_code(self.student_file, [])
        with open(os.path.join(tmp_path, "renamed_copy.txt"), "r") as f:
            content = f.read()
        assert "Это оригинальный файл." in content
