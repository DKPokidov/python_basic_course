# tests/test_04_paradigms/test_task3_find_overloaded.py
"""
Тесты для задания 3: Поиск перегруженных объектов
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


class TestTask3FindOverloaded:
    """Тесты для задания 3: Поиск перегруженных объектов"""

    student_file = get_module07_file('task3_find_overloaded.py')

    def test_threshold_500(self):
        mod = load_student_code(self.student_file)
        result = mod.find_overloaded(city_data, 500)
        assert result == ["Гимназия №5 (850 мест)", "Средняя школа №8 (600 мест)"]

    def test_threshold_300(self):
        mod = load_student_code(self.student_file)
        result = mod.find_overloaded(city_data, 300)
        assert len(result) == 3
        assert "Гимназия №5 (850 мест)" in result
        assert "Городская больница №2 (320 мест)" in result
        assert "Средняя школа №8 (600 мест)" in result

    def test_threshold_100(self):
        mod = load_student_code(self.student_file)
        result = mod.find_overloaded(city_data, 100)
        assert len(result) == 4

    def test_threshold_0_returns_all(self):
        mod = load_student_code(self.student_file)
        result = mod.find_overloaded(city_data, 0)
        assert len(result) == 5

    def test_format_string(self):
        mod = load_student_code(self.student_file)
        result = mod.find_overloaded(city_data, 800)
        assert "Гимназия №5" in result[0]
        assert "850 мест" in result[0]
