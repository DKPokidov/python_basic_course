# tests/test_05_api/test_task2_parse_currency.py
"""
Тесты для задания 2: Парсинг курсов валют
"""

import pytest

from tests.test_05_api.conftest import load_student_code, get_module10_file

SAMPLE_DATA = {
    'ValCurs': {
        '@Date': '28.02.2026',
        'Valute': [
            {'CharCode': 'USD', 'Nominal': '1', 'Name': 'Доллар США',
             'Value': '77,2736', 'VunitRate': '77,2736'},
            {'CharCode': 'EUR', 'Nominal': '1', 'Name': 'Евро',
             'Value': '91,2965', 'VunitRate': '91,2965'},
            {'CharCode': 'JPY', 'Nominal': '100', 'Name': 'Иен',
             'Value': '49,6107', 'VunitRate': '0,496107'},
            {'CharCode': 'GBP', 'Nominal': '1', 'Name': 'Фунт стерлингов',
             'Value': '104,4353', 'VunitRate': '104,4353'},
        ],
    },
}


@pytest.fixture(scope='module')
def module():
    return load_student_code(get_module10_file('task2_parse_currency.py'))


class TestGetCurrencyRate:
    """Тесты функции get_currency_rate"""

    def test_usd(self, module):
        assert module.get_currency_rate(SAMPLE_DATA, 'USD') == 77.2736

    def test_eur(self, module):
        assert module.get_currency_rate(SAMPLE_DATA, 'EUR') == 91.2965

    def test_jpy_uses_vunitrate(self, module):
        # JPY имеет Nominal=100, поэтому VunitRate (0.496107), а не Value
        assert module.get_currency_rate(SAMPLE_DATA, 'JPY') == pytest.approx(0.496107)

    def test_not_found(self, module):
        assert module.get_currency_rate(SAMPLE_DATA, 'XXX') is None


class TestGetAllRates:
    """Тесты функции get_all_rates"""

    def test_all_rates(self, module):
        rates = module.get_all_rates(SAMPLE_DATA)
        assert rates == {
            'USD': 77.2736,
            'EUR': 91.2965,
            'JPY': pytest.approx(0.496107),
            'GBP': 104.4353,
        }

    def test_all_rates_keys(self, module):
        rates = module.get_all_rates(SAMPLE_DATA)
        assert set(rates.keys()) == {'USD', 'EUR', 'JPY', 'GBP'}
