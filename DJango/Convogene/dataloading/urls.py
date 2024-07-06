from django.urls import path
from .views import webscrapping

urlpatterns = [
    path('web-scrapping',webscrapping,name='web-scrapping')
]