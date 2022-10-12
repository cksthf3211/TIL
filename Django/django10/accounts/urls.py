from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('home/', views.home, name="home"),
    path('<int:pk>', views.detail, name="detail"),
    path('member/', views.member, name="member"),
    path('login/', views.login, name="login"),
]
