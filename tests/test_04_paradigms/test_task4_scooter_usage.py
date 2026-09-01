# tests/test_04_paradigms/test_task4_scooter_usage.py
"""
Тесты для задания 4: Анализ использования городских электросамокатов
"""

import importlib.util
from tests.test_04_paradigms.conftest import get_module06_file


def load_student_code(student_file):
    spec = importlib.util.spec_from_file_location("student_module", student_file)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class TestTask4ScooterUsage:
    """Тесты для задания 4: Анализ использования городских электросамокатов"""

    student_file = get_module06_file('task4_scooter_usage.py')

    def test_basic(self):
        mod = load_student_code(self.student_file)
        data = [{"user_id": 1, "duration_min": 30, "distance_km": 10.5, "start_zone": "Центр"}]
        result = mod.analyze_scooter_usage(data)
        assert result[0]["speed_kmh"] == 21.0

    def test_zero_duration(self):
        mod = load_student_code(self.student_file)
        data = [{"user_id": 2, "duration_min": 0, "distance_km": 0.0, "start_zone": "Север"}]
        result = mod.analyze_scooter_usage(data)
        assert result[0]["speed_kmh"] == 0.0

    def test_multiple_rides(self):
        mod = load_student_code(self.student_file)
        data = [{"user_id": 1, "duration_min": 20, "distance_km": 5.0, "start_zone": "Центр"}, {"user_id": 2, "duration_min": 45, "distance_km": 15.0, "start_zone": "Юг"}]
        result = mod.analyze_scooter_usage(data)
        assert result[0]["speed_kmh"] == 15.0
        assert result[1]["speed_kmh"] == 20.0

    def test_rounding(self):
        mod = load_student_code(self.student_file)
        data = [{"user_id": 1, "duration_min": 3, "distance_km": 1.0, "start_zone": "Запад"}]
        result = mod.analyze_scooter_usage(data)
        assert result[0]["speed_kmh"] == 20.0

    def test_original_data_preserved(self):
        mod = load_student_code(self.student_file)
        data = [{"user_id": 1, "duration_min": 10, "distance_km": 3.0, "start_zone": "Восток"}]
        result = mod.analyze_scooter_usage(data)
        assert result[0]["user_id"] == 1
        assert result[0]["start_zone"] == "Восток"
