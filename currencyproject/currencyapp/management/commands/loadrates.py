from django.core.management.base import BaseCommand
import requests
from currencyapp.models import Currency, Rate
import datetime

class Command(BaseCommand):

    def handle(self, *args, **options):
        currencies = Currency.objects.all()
        current_date = datetime.date.today().strftime('%Y-%m-%d')
        for item in currencies:
            data = requests.get('https://api-pub.bitfinex.com/v2/candles/trade:1D:t%sUSD/hist'%item.name)
            data = data.json()
            for candle in data:
                new_candle = Rate(currency_id = item, date=current_date, rate=candle[2], volume=candle[5])
                new_candle.save()