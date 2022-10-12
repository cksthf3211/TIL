from django.shortcuts import render, redirect
from accounts.forms import UsersForm
from .models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def home (request):
    return render(request, "accounts/home.html")

def signup(request):
    if request.method == "POST":
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("accounts:home")
    else:
        form = UsersForm()
    context = {
        'form' : form,
    }
    return render(request, "accounts/signup.html", context)

def detail(request, pk):
    k = User.objects.get(pk=pk)
    context = {
        "k" : k,
    }
    return render(request, "accounts/detail.html", context)

def member(request):
    t = User.objects.all()
    context = {
        't' : t
    }
    return render(request, 'accounts/member.html', context)

def login(request):
    form = AuthenticationForm()
    if 
    context = {
        'form' : form
    }
    return render(request, "accounts/login.html", context)

def logout(request):
    return render(request, "accounts/logout.html")