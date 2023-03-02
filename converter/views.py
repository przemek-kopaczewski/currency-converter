import requests
from django.shortcuts import render


def get_exchange_rates():
    url = "http://api.nbp.pl/api/exchangerates/tables/a?format=json"
    response = requests.get(url)
    data = response.json()
    return data[0]['rates']


def pln_to_currency(pln, currency_type, rates):
    for rate in rates:
        if rate['code'] == currency_type:
            result = float(pln) / float(rate['mid'])
            return round(result, 2)
    return None


def currency_to_pln(val, currency_type, rates):
    for rate in rates:
        if rate['code'] == currency_type:
            result = float(val) * float(rate['mid'])
            return round(result, 2)
    return None


def base(request):
    template_name = 'converter/base.html'
    rates = get_exchange_rates()
    result = None

    if request.method == "POST":
        pln = request.POST.get('pln')
        val = request.POST.get('val')
        currency_type = request.POST.get('currency_type')

        if pln:
            result = pln_to_currency(pln, currency_type, rates)
        elif val:
            result = currency_to_pln(val, currency_type, rates)

    return render(request, template_name, {'result': result, 'rates': rates})
