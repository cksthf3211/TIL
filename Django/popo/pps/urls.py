from django.urls import path
from . import views

app_name = 'pps'


urlpatterns = [
    path('index/', views.index, name='index.html'),
    path('new/', views.new, name='new.html'),
    path('create/', views.create, name='create.html'),
]