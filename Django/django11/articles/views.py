from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm # Django 내장 로그인 폼 AuthenticationForm 활용
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from . forms import UsersForm
from . forms import zzUserChangeForm
from . models import User

# Create your views here.

def home(request):
    return render(request, 'articles/home.html')

def signup(request):
    if request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:home')
    else:
        form = UsersForm()
    context = {
        'form' : form
    }
            
    return render(request, 'articles/signup.html', context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'articles:home')
    else:
        form = AuthenticationForm()
    context = {
        'form' : form
    }
    return render(request, 'articles/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('articles:home')

def member(request):
    m = User.objects.all()
    context = {
        'm' : m
    }
    return render(request, "articles/member.html", context)

def detail(request, pk):
    d = User.objects.get(pk=pk)
    context = {
        'd' : d
    }
    return render(request, 'articles/detail.html', context)

def update(request):
    if request.method == 'POST':
        u = zzUserChangeForm(request.POST, instance=request.user)
        if u.is_valid():
            u.save()
            return redirect('articles:detail', request.user.pk)
    else:
        u = zzUserChangeForm(instance=request.user)
    context = {
        'u' : u
    }
    return render(request, 'articles/update.html', context)

def delete(request, pk):
    dd = User.objects.get(pk=pk)
    dd.delete()
    return redirect('articles:member')