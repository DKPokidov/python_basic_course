# tests/test_04_paradigms/test_task5_geospatial.py
"""
Тесты для задания 5: Геопространственный анализ
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


class TestTask5Geospatial:
    """Тесты для задания 5: Геопространственный анализ"""

    student_file = get_module07_file('task5_geospatial.py')

    def test_returns_list(self):
        mod = load_student_code(self.student_file)
        result = mod.find_least_served_districts(city_data)
        assert isinstance(result, list)

    def test_result_length(self):
        mod = load_student_code(self.student_file)
        result = mod.find_least_served_districts(city_data)
        assert len(result) <= 3

    def test_sorted_by_density(self):
        mod = load_student_code(self.student_file)
        result = mod.find_least_served_districts(city_data)
        densities = [item[1] for item in result]
        assert densities == sorted(densities)

    def test_all_three_districts_present(self):
        mod = load_student_code(self.student_file)
        result = mod.find_least_served_districts(city_data)
        districts = {item[0] for item in result}
        assert "Центральный" in districts
        assert "Южный" in districts
        assert "Западный" in districts

    def test_tuples_of_two(self):
        mod = load_student_code(self.student_file)
        result = mod.find_least_served_districts(city_data)
        for item in result:
            assert isinstance(item, tuple)
            assert len(item) == 2
            assert isinstance(item[0], str)
            assert isinstance(item[1], (int, float))

    def test_density_positive(self):
        mod = load_student_code(self.student_file)
        result = mod.find_least_served_districts(city_data)
        for item in result:
            assert item[1] > 0
