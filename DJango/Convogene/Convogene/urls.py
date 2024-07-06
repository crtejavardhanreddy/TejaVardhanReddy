from django.contrib import admin
from django.urls import path, include
from .views import home_page, landing_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('dataloading.urls')),
    path('',landing_page,name='Land'),
    path('home/',home_page,name='Home')
]
