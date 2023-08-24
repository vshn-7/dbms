from django.urls import path
from . import views


urlpatterns = [
    path('hello/',views.say_hello, name = 'hello'),
    path('index', views.index, name='index'),
    path('', views.home, name='home'), 
    path('Login', views.Login, name='Login'), 
    path('queryp',views.queryp,name = 'queryp'),


]
