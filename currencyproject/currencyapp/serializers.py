from .models import Currency, Rate
from rest_framework import serializers

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ('id', 'name')

class RateSerializer(serializers.Serializer):
    last_rate = serializers.DecimalField(max_digits=20, decimal_places=8)
    avg_volume = serializers.DecimalField(max_digits=20, decimal_places=8)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass