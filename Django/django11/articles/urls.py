from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('home/', views.home, name="home"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('member/', views.member, name="member"),
    path('<int:pk>/', views.detail, name="detail"),
    path('update/', views.update, name="update"),
    path('delete/<int:pk>/', views.delete, name="delete"),
]