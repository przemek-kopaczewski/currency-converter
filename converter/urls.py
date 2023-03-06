from django.urls import path
from .views import main_converter

urlpatterns = [
    path('', main_converter, name="main_converter"),
]
