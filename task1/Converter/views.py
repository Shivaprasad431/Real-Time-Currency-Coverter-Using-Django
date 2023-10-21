# Converter/views.py
from django.shortcuts import render
import requests

def convert_currency(request):
    if request.method == 'POST':
        from_currency = request.POST.get('from_currency')
        to_currency = request.POST.get('to_currency')
        amount = float(request.POST.get('amount'))

        # Replace 'YOUR_API_KEY' with your actual Open Exchange Rates API key
        api_key = 'faa3396544abb70e8f3975be'
        base_url = f'https://open.er-api.com/v6/latest/{from_currency}?apikey={api_key}'

        try:
            # Fetch latest exchange rates
            response = requests.get(base_url,timeout=10)
            data = response.json()

            # Get the exchange rate for the 'to_currency'
            exchange_rate = data['rates'][to_currency]

            # Calculate the converted amount
            converted_amount = amount * exchange_rate

            context = {
                'from_currency': from_currency,
                'to_currency': to_currency,
                'amount': amount,
                'converted_amount': converted_amount,
            }
        except Exception as e:
            error_message = f"Error fetching exchange rates: {e} Enter in ISO standard of a Country Currency"
            context = {'error_message': error_message}

        return render(request, 'Converter/convert_currency.html', context)

    return render(request, 'Converter/convert_currency.html')
