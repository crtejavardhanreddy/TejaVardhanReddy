from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def webscrape(request):
    return HttpResponse('<h1>Web scrapping done</h1>')