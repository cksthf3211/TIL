from django.shortcuts import render, redirect
from .models import User
from .forms import CustomUserChangeForm
from .forms import CustomUserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def index(request):
    users = User.objects.all()
    context = {
        "users" : users
    }
    return render(request, 'accounts/index.html', context)

def signup(request):
    form = CustomUserCreationForm()

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            ## 회원 가입 후 로그인
            auth_login(request, user)
            return redirect('accounts:index')
    
    context = {
        "form" : form
    }
    return render(request, 'accounts/signup.html', context)

def detail(request, pk):
    d = User.objects.get(pk=pk)
    context ={
        'd' : d,
    }
    return render(request,'accounts/detail.html', context)

def update (request):
    form = CustomUserChangeForm(instance=request.user)
    
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:detail', request.user.pk)

    context ={
        'form' : form
    }
    return render(request, 'accounts/update.html', context)

def login(request):
    form = AuthenticationForm()
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'accounts:index')
    context = {
        'form' : form
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('accounts:index')

def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request)

    return redirect('accounts:index')