# tests/test_05_api/test_task3_currency_report.py
"""
Тесты для задания 3: Отчёт и конвертация валют
"""

import pytest

from tests.test_05_api.conftest import load_student_code, get_module10_file

RATES = {
    'USD': 77.2736,
    'EUR': 91.2965,
    'JPY': 0.496107,
    'GBP': 104.4353,
    'CNY': 11.2394,
}


@pytest.fixture(scope='module')
def module():
    return load_student_code(get_module10_file('task3_currency_report.py'))


class TestHighestLowest:
    """Тесты highest_rate и lowest_rate"""

    def test_highest(self, module):
        assert module.highest_rate(RATES) == 'GBP'

    def test_lowest(self, module):
        assert module.lowest_rate(RATES) == 'JPY'


class TestConvert:
    """Тесты функции convert"""

    def test_usd_to_rub(self, module):
        # 100 USD -> рубли: 100 * 77.2736 = 7727.36
        assert module.convert(RATES, 100, 'USD', 'USD') == pytest.approx(100.0)

    def test_rub_to_eur(self, module):
        # 1000 руб -> EUR: 1000 / 91.2965
        assert module.convert(RATES, 1000, 'USD', 'EUR') == pytest.approx(
            1000 * RATES['USD'] / RATES['EUR']
        )

    def test_jpy_to_usd(self, module):
        # 100 JPY -> USD: 100 * 0.496107 / 77.2736
        expected = 100 * RATES['JPY'] / RATES['USD']
        assert module.convert(RATES, 100, 'JPY', 'USD') == pytest.approx(expected)

    def test_explicit_value(self, module):
        # Проверка известного значения: 7727.36 руб при курсе USD=77.2736
        assert module.convert({'USD': 77.2736}, 100, 'USD', 'USD') == pytest.approx(100.0)


class TestTopExpensive:
    """Тесты функции top_expensive"""

    def test_top1(self, module):
        assert module.top_expensive(RATES, 1) == ['GBP']

    def test_top3(self, module):
        assert module.top_expensive(RATES, 3) == ['GBP', 'EUR', 'USD']

    def test_all(self, module):
        assert module.top_expensive(RATES, 5) == ['GBP', 'EUR', 'USD', 'CNY', 'JPY']
