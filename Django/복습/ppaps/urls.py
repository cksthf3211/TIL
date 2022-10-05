from django.contrib import admin
from django.urls import path
from . import views

app_name = 'ppaps'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('detail/<int:pk>', views.detail, name='detail'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('update/<int:pk>', views.update, name='update'),
]