# tests/test_module06/test_task3_park_analysis.py
"""
Тесты для задания 3: Анализ загруженности городских парков
"""

import importlib.util
from tests.test_module06.conftest import get_module06_file


def load_student_code(student_file):
    spec = importlib.util.spec_from_file_location("student_module", student_file)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class TestTask3ParkAnalysis:
    """Тесты для задания 3: Анализ загруженности городских парков"""

    student_file = get_module06_file('task3_park_analysis.py')

    def test_overloaded(self):
        mod = load_student_code(self.student_file)
        data = {"Парк Победы": {"visitors_day": 6000, "area_ha": 100, "entrances": 4}}
        result = mod.analyze_park(data)
        assert result["Парк Победы"]["density"] == 60.0
        assert result["Парк Победы"]["entrance_load"] == 1500
        assert result["Парк Победы"]["status"] == "перегружен"

    def test_normal(self):
        mod = load_student_code(self.student_file)
        data = {"Парк Культуры": {"visitors_day": 2000, "area_ha": 80, "entrances": 3}}
        result = mod.analyze_park(data)
        assert result["Парк Культуры"]["density"] == 25.0
        assert result["Парк Культуры"]["entrance_load"] == 667
        assert result["Парк Культуры"]["status"] == "в норме"

    def test_custom_threshold(self):
        mod = load_student_code(self.student_file)
        data = {"Парк Лесного": {"visitors_day": 3000, "area_ha": 100, "entrances": 2}}
        result = mod.analyze_park(data, threshold=30)
        assert result["Парк Лесного"]["density"] == 30.0
        assert result["Парк Лесного"]["status"] == "в норме"

    def test_multiple_parks(self):
        mod = load_student_code(self.student_file)
        data = {"Парк А": {"visitors_day": 6000, "area_ha": 50, "entrances": 5}, "Парк Б": {"visitors_day": 1000, "area_ha": 100, "entrances": 2}}
        result = mod.analyze_park(data)
        assert result["Парк А"]["status"] == "перегружен"
        assert result["Парк Б"]["status"] == "в норме"
