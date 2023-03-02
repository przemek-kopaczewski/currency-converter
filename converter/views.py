from django.shortcuts import render
import requests


def get_exchange_rates():
    url = "http://api.nbp.pl/api/exchangerates/tables/a?format=json"
    response = requests.get(url)
    data = response.json()
    return data[0]['rates']


def converter(pln, currency_type, rates):
    for rate in rates:
        if rate['code'] == currency_type:
            result = float(pln) / float(rate['mid'])
            return round(result, 2)
    return None


def base(request):
    template_name = 'converter/base.html'

    if request.method == "POST":
        pln = request.POST['pln']
        currency_type = request.POST.get('currency_type')
        rates = get_exchange_rates()
        result = converter(pln, currency_type, rates)
        return render(request, template_name, {'result': result, 'rates': rates})

    rates = get_exchange_rates()
    return render(request, template_name, {'rates': rates})
