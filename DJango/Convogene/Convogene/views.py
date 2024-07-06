from django.http import HttpResponse

def landing_page(request):
    return HttpResponse('<h1>This is Landing page</h1>')

def home_page(request):
    return HttpResponse('<h1>Welcome to Convogene</h1>')