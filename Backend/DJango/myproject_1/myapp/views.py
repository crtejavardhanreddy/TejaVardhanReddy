from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse('<h1>Hi</h1>')

def upload(request):
    return HttpResponse('<h2>Good morning</h2>')