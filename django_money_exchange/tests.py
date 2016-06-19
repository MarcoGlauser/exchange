import datetime

from django.test import TestCase
from django_money_exchange.models import ExchangeRate, OpenExchangeRatesProvider
from django_money_exchange.utils import calculate_direct_exchange_rate
from moneyed import CHF, USD, AUD, EUR


class ConversionTestCase(TestCase):
    def setUp(self):
        pass

    def test_calculate_direct_exchange_rate_with_same_base(self):
        chf_exchange_rate = 0.9
        aud_exchange_rate = 1.4
        calculated_direct_exchange_rate = calculate_direct_exchange_rate(chf_exchange_rate,aud_exchange_rate)
        self.assertAlmostEqual(0.6428571,calculated_direct_exchange_rate,7,None,None)

    def test_asdf(self):
        asdf = OpenExchangeRatesProvider()
        asdf.get_rates_for_date(datetime.date.today())