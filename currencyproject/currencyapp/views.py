from .models import Currency, Rate
from rest_framework import viewsets, permissions, status
from .serializers import CurrencySerializer, RateSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
import datetime


class CurrencyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    permission_classes = (permissions.IsAuthenticated,)

class LastRate(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def get(self, request, curr_id):
        needed_date = datetime.date.today() - datetime.timedelta(days=10)
        needed_date = needed_date.strftime('%Y-%m-%d')
        data = Rate.get_rate_data(needed_date, curr_id)
        clean_data(data)
        serializer = RateSerializer(data=data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def clean_data(data: dict):
    for key, value in data.items():
        if value is None:
            data[key] = 0