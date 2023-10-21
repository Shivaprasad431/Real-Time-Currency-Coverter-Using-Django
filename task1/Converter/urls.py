from django.urls import path
from .views import convert_currency

app_name = 'Converter'

urlpatterns = [
    path('', convert_currency, name='convert_currency'),
    # Other URL patterns if any
]
