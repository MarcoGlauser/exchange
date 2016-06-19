import datetime
from django_money_exchange.models import ExchangeRate
from moneyed import Money, Currency


def convert_money(source: Money, target: Currency, date: datetime.date = datetime.date.today()) -> Money:
    if source.currency == target:
        return source
    exchange_rate = get_or_fetch_direct_exchange_rate(source.currency, target, date)
    target_amount = source.amount / exchange_rate
    return Money(target_amount, target)


def get_or_fetch_direct_exchange_rate(source: Currency, target: Currency, date=datetime.date):
    try:
        source_rate = ExchangeRate.objects.get(currency=source, date=date)
        target_rate = ExchangeRate.objects.get(currency=target, date=date)
    except ExchangeRate.DoesNotExist:
        # todo get exchange rate
        pass
    return calculate_direct_exchange_rate(source_rate.exchange_rate, target_rate.exchange_rate)

def calculate_direct_exchange_rate(source_rate: float, target_rate: float):
    return source_rate / target_rate
