"""blackpjt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from darks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('is_odd_even/<int:_number>', views.is_odd_even),             # 1번
    path('calculate/<int:_number1>/<int:_number2>', views.calculate), # 2번
    path('form_/', views.form_),                                      # 3번
    path('form_2/', views.form_2),                                     # 3번
    path('lipsum/', views.lipsum),                             # 4번
    path('lipsum_2/', views.lipsum_2),                             # 4번
]
