from django.test import SimpleTestCase
from django.urls import reverse, resolve
from converter.views import main_converter


class TestUrls(SimpleTestCase):

    def test_converter_url_resolved(self):
        url = reverse('main_converter')
        self.assertEquals(resolve(url).func, main_converter)
