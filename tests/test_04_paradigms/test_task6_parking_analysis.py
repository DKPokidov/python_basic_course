# tests/test_04_paradigms/test_task6_parking_analysis.py
"""
Тесты для задания 6: Анализ загруженности городских парковок
"""

from tests.test_04_paradigms.conftest import run_student_code, get_module06_file


class TestTask6ParkingAnalysis:
    """Тесты для задания 6: Анализ загруженности городских парковок"""

    student_file = get_module06_file('task6_parking_analysis.py')

    def test_high_load_parkings(self, monkeypatch, tmp_path):
        deep_dir = tmp_path / "a" / "b"
        deep_dir.mkdir(parents=True)
        data_dir = tmp_path / "data"
        data_dir.mkdir()
        parkings_content = "название_парковки;вместимость;занято\nПарковка_1;100;90\nПарковка_2;200;150\nПарковка_3;50;50\n"
        (data_dir / "parkings.txt").write_text(parkings_content, encoding="utf-8")
        monkeypatch.chdir(deep_dir)
        run_student_code(self.student_file, [])
        output_file = data_dir / "high_load_parkings.txt"
        assert output_file.exists()
        content = output_file.read_text(encoding="utf-8")
        assert "название_парковки;вместимость;занято;занятость_%" in content
        assert "Парковка_1;100;90;90.0" in content
        assert "Парковка_2;200;150;75.0" not in content
        assert "Парковка_3;50;50;100.0" in content

    def test_no_high_load(self, monkeypatch, tmp_path):
        deep_dir = tmp_path / "a" / "b"
        deep_dir.mkdir(parents=True)
        data_dir = tmp_path / "data"
        data_dir.mkdir()
        parkings_content = "название_парковки;вместимость;занято\nПарковка_1;100;50\nПарковка_2;200;100\n"
        (data_dir / "parkings.txt").write_text(parkings_content, encoding="utf-8")
        monkeypatch.chdir(deep_dir)
        run_student_code(self.student_file, [])
        output_file = data_dir / "high_load_parkings.txt"
        assert output_file.exists()
        content = output_file.read_text(encoding="utf-8")
        lines = content.strip().split("\n")
        assert len(lines) == 1
