from django.urls import path
from . import views

# urlpatters is a keyword
urlpatterns = [
    # route should not start with '/' and should end with '/'
    path("home/",views.index,name='index'),
    path("upload_doc/",views.upload,name='doc_upload')
]