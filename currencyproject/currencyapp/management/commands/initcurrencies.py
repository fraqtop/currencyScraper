from django.core.management.base import BaseCommand
from currencyapp.models import Currency

class Command(BaseCommand):
    def handle(self, *args, **options):
        for currency in ['BTC', 'ETH', 'BCH', 'LTC', 'XRP', 'BNB', 'ETC', 'TRX']:
            new_currency = Currency(name = currency)
            new_currency.save()