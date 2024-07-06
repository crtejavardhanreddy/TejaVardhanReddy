from django.urls import path
from . import views

# urlpatters is a keyword
urlpatterns = [
    # route should not start with '/' and should end with '/'
    path("land/",views.index,name='land'),
    path("upload_doc",views.upload_doc,name='upload_doc'),
    path("register",views.register,name='register'),
    path("login",views.Login,name='login'),
    path("logout",views.Logout,name='logout'),
    path("post/<str:pk>",views.posts,name='post'),
    path('counter',views.counter,name='counter')
]