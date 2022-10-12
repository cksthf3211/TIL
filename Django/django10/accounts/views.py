from django.shortcuts import render, redirect
from accounts.forms import UsersForm
from .models import User
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
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
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('accounts:member')
        
    else:
        form = AuthenticationForm()
    context = {
        'form' : form
    }
    return render(request, "accounts/login.html", context)

def logout(request):
    auth_logout(request)
    return redirect('accounts:member')