# tests/test_module10/test_task1_fetch_rates.py
"""
Тесты для задания 1: Получение курсов валют с сайта ЦБ РФ
"""

from unittest.mock import patch

from tests.test_module10.conftest import load_student_code, get_module10_file

SAMPLE_XML = """<?xml version="1.0" encoding="windows-1251"?>
<ValCurs Date="28.02.2026" name="Foreign Currency Market">
  <Valute ID="R01235">
    <NumCode>840</NumCode><CharCode>USD</CharCode><Nominal>1</Nominal>
    <Name>Доллар США</Name><Value>77,2736</Value><VunitRate>77,2736</VunitRate>
  </Valute>
</ValCurs>""".encode('utf-8')


class TestTask1FetchRates:
    """Тесты для задания 1: Получение курсов валют"""

    student_file = get_module10_file('task1_fetch_rates.py')

    def test_fetch_success(self):
        mod = load_student_code(self.student_file)

        class FakeResponse:
            content = SAMPLE_XML

            def raise_for_status(self):
                return None

        with patch('requests.get', return_value=FakeResponse()) as mock_get:
            result = mod.fetch_rates()

        mock_get.assert_called_once()
        assert result is not None
        assert result['ValCurs']['Valute']['CharCode'] == 'USD'

    def test_fetch_returns_none_on_bad_response(self):
        mod = load_student_code(self.student_file)

        import requests

        class FakeBadResponse:
            content = None

            def raise_for_status(self):
                raise requests.exceptions.HTTPError('500 Server Error')

        with patch('requests.get', return_value=FakeBadResponse()):
            result = mod.fetch_rates()

        assert result is None

    def test_fetch_passes_url(self):
        mod = load_student_code(self.student_file)

        class FakeResponse:
            content = SAMPLE_XML

            def raise_for_status(self):
                return None

        with patch('requests.get', return_value=FakeResponse()) as mock_get:
            mod.fetch_rates('http://example.test/xml')

        mock_get.assert_called_once_with('http://example.test/xml', timeout=10)
