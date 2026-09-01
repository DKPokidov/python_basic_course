# tests/test_04_paradigms/test_task2_accessibility_analysis.py
"""
Тесты для задания 2: Анализ доступности
"""

import importlib.util
from tests.test_04_paradigms.conftest import get_module07_file


def load_student_code(student_file):
    spec = importlib.util.spec_from_file_location("student_module", student_file)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


city_data = {
    "city": "Новоград",
    "year": 2024,
    "objects": [
        {"id": 101, "type": "school", "name": "Гимназия №5", "district": "Центральный", "capacity": 850, "coordinates": [55.751244, 37.618423], "accessibility": {"parking": True, "elevator": False, "ramp": True}, "services": ["дошкольная_группа", "спортзал", "столовая"]},
        {"id": 102, "type": "hospital", "name": "Городская больница №2", "district": "Южный", "capacity": 320, "coordinates": [55.749231, 37.620111], "accessibility": {"parking": True, "elevator": True, "ramp": True}, "services": ["травмпункт", "стационар", "диагностика"]},
        {"id": 103, "type": "kindergarten", "name": "Детский сад №15 «Солнышко»", "district": "Центральный", "capacity": 120, "coordinates": [55.7521, 37.6195], "accessibility": {"parking": False, "elevator": False, "ramp": True}, "services": ["ясельная_группа", "логопед", "бассейн", "продлёнка"]},
        {"id": 104, "type": "school", "name": "Средняя школа №8", "district": "Западный", "capacity": 600, "coordinates": [55.745000, 37.630000], "accessibility": {"parking": True, "elevator": True, "ramp": False}, "services": ["библиотека", "актовый_зал", "столовая"]},
        {"id": 105, "type": "kindergarten", "name": "Детский сад №22 «Радуга»", "district": "Южный", "capacity": 90, "coordinates": [55.750000, 37.625000], "accessibility": {"parking": True, "elevator": False, "ramp": True}, "services": ["ясельная_группа", "музыкальный_зал", "продлёнка"]}
    ]
}


class TestTask2AccessibilityAnalysis:
    """Тесты для задания 2: Анализ доступности"""

    student_file = get_module07_file('task2_accessibility_analysis.py')

    def test_result_is_dict(self):
        mod = load_student_code(self.student_file)
        result = mod.accessibility_analysis(city_data)
        assert isinstance(result, dict)

    def test_central_district(self):
        mod = load_student_code(self.student_file)
        result = mod.accessibility_analysis(city_data)
        assert result.get("Центральный") == 2

    def test_southern_district(self):
        mod = load_student_code(self.student_file)
        result = mod.accessibility_analysis(city_data)
        assert result.get("Южный") == 2

    def test_western_district_absent(self):
        mod = load_student_code(self.student_file)
        result = mod.accessibility_analysis(city_data)
        assert "Западный" not in result

    def test_total_count(self):
        mod = load_student_code(self.student_file)
        result = mod.accessibility_analysis(city_data)
        assert sum(result.values()) == 4
