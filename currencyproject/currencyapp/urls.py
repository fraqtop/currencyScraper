from django.urls import path, include
from rest_framework import routers
from .views import CurrencyViewSet, LastRate

router = routers.DefaultRouter()
router.register(r'currencies', CurrencyViewSet)

urlpatterns = [
    path('rate/<int:curr_id>', LastRate.as_view()),
    path('', include(router.urls))
]