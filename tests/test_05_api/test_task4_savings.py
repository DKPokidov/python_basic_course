# tests/test_05_api/test_task4_savings.py
"""
Тесты для задания 4: Прикладная задача — планирование путешествия
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

RATES_TODAY = {
    'USD': 77.2736,
    'EUR': 91.2965,
    'JPY': 0.496107,
}

RATES_YESTERDAY = {
    'USD': 78.10,
    'EUR': 90.50,
    'JPY': 0.496107,
}


@pytest.fixture(scope='module')
def module():
    return load_student_code(get_module10_file('task4_savings.py'))


class TestBestCurrencyToTravel:
    """Тесты функции best_currency_to_travel"""

    def test_best_is_jpy(self, module):
        # У JPY самый низкий курс -> за бюджет получим больше всего
        assert module.best_currency_to_travel(RATES, 10000) == 'JPY'

    def test_with_minimal_set(self, module):
        rates = {'USD': 80.0, 'EUR': 90.0}
        assert module.best_currency_to_travel(rates, 5000) == 'USD'


class TestHowMuchYouGet:
    """Тесты функции how_much_you_get"""

    def test_usd(self, module):
        assert module.how_much_you_get(RATES, 7727.36, 'USD') == pytest.approx(100.0)

    def test_budget_division(self, module):
        assert module.how_much_you_get(RATES, 1000, 'USD') == pytest.approx(1000 / RATES['USD'])


class TestCurrencyTrend:
    """Тесты функции currency_trend"""

    def test_up(self, module):
        res = module.currency_trend(RATES_TODAY, RATES_YESTERDAY, 'EUR')
        assert res['code'] == 'EUR'
        assert res['today'] == 91.2965
        assert res['yesterday'] == 90.50
        assert res['change'] == pytest.approx(0.7965)
        assert res['direction'] == 'up'

    def test_down(self, module):
        res = module.currency_trend(RATES_TODAY, RATES_YESTERDAY, 'USD')
        assert res['code'] == 'USD'
        assert res['change'] == pytest.approx(77.2736 - 78.10)
        assert res['direction'] == 'down'

    def test_same(self, module):
        res = module.currency_trend(RATES_TODAY, RATES_YESTERDAY, 'JPY')
        assert res['change'] == 0.0
        assert res['direction'] == 'same'


class TestFormatRateTable:
    """Тесты функции format_rate_table"""

    def test_content(self, module):
        table = module.format_rate_table({'USD': 77.2736, 'JPY': 0.496107})
        # Строки отсортированы по возрастанию курса: JPY дешевле USD
        lines = table.split('\n')
        assert lines[0] == 'JPY: 0.50 руб.'
        assert lines[1] == 'USD: 77.27 руб.'

    def test_newline_separated(self, module):
        table = module.format_rate_table({'USD': 77.2736, 'EUR': 91.2965})
        assert '\n' in table
