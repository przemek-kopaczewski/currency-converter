import requests
from django.shortcuts import render


def get_exchange_rates():
    url = "http://api.nbp.pl/api/exchangerates/tables/a?format=json"
    response = requests.get(url)
    data = response.json()
    return data[0]['rates']


def pln_to_currency(pln_value, currency_type, rates):
    for rate in rates:
        if rate['code'] == currency_type:
            result = float(pln_value) / float(rate['mid'])
            return round(result, 4)
    return None


def currency_to_pln(currency_value, currency_type, rates):
    for rate in rates:
        if rate['code'] == currency_type:
            result = float(currency_value) * float(rate['mid'])
            return round(result, 4)
    return None


def main_converter(request):
    template_name = 'converter/base.html'
    rates = get_exchange_rates()
    result = None
    exchange_type = ""
    currency_type = None

    if request.method == "POST":
        pln_value = request.POST.get('pln_value')
        currency_value = request.POST.get('currency_value')

        if pln_value:
            currency_type = request.POST.get('pln_to_currency_type')
            result = pln_to_currency(pln_value, currency_type, rates)
            exchange_type = 'pln_to_currency'
        elif currency_value:
            currency_type = request.POST.get('currency_type_to_pln')
            result = currency_to_pln(currency_value, currency_type, rates)
            exchange_type = 'currency_to_pln'

    context = {
        'result': result,
        'rates': rates,
        'exchange_type': exchange_type,
        'currency': currency_type,
    }
    return render(request, template_name, context)
