import datetime

import requests
from django.db import models
from djmoney.models.fields import CurrencyField
# Create your models here.

class ExchangeRate(models.Model):
    date = models.DateField()
    currency = CurrencyField()
    base_currency = CurrencyField()
    exchange_rate = models.FloatField()

class ExchangeRateProvider(object):

    def update_rates(self,date:datetime.date=datetime.date.today()):
        self.get_rates_for_date(date)

    def get_rates_for_date(self, date:datetime.date):
        raise NotImplementedError

class OpenExchangeRatesProvider(ExchangeRateProvider):
    base_url = 'https://openexchangerates.org/api/'
    app_id = '27f620bfc6be4c76b4d34ef17663f741'

    def get_rates_for_date(self, date:datetime.date):
        date_string = date.strftime('%Y-%m-%d')
        params = {'app_id':self.app_id}
        response = requests.get('{base}historical/{date}.json'.format(base=self.base_url,date=date_string),params=params)
        print(response.json())