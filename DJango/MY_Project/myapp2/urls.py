from django.urls import path
from . import views

urlpatterns = [
    path('webscrapping/',views.webscrape,name='webscrape')
]