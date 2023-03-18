from django.test import TestCase
from converter.views import get_exchange_rates, pln_to_currency, currency_to_pln
from converter.urls import main_converter


class TestViews(TestCase):

    def test_get_exchange_rates(self):
        self.assertIsNotNone(get_exchange_rates)

    def test_pln_to_currency(self):
        for rate in get_exchange_rates():
            self.assertTrue(pln_to_currency(1, rate['code'], get_exchange_rates()))

    def test_currency_to_pln(self):
        for rate in get_exchange_rates():
            self.assertTrue(currency_to_pln(1, rate['code'], get_exchange_rates()))
