from django.shortcuts import render, redirect
from .models import User
from .forms import CustomUserChangeForm
from .forms import CustomUserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from articles.models import Article, Comment
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import get_user_model
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
    user_article = d.article_set.all()
    context ={
        'd' : d,
        'user_article':user_article,
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

def follow(request, pk):
    # 프로필에 해당하는 유저를 로그인한 유저가!
    user = get_object_or_404(get_user_model(), pk=pk)
    if request.user == user:
        messages.warning(request, '스스로 팔로우 할 수 없습니다.')
        return redirect('accounts:detail', pk)
    if request.user in user.followers.all():
    # (이미) 팔로우 상태이면, '팔로우 취소'버튼을 누르면 삭제 (remove)
        user.followers.remove(request.user)
    else:
    # 팔로우 상태가 아니면, '팔로우'를 누르면 추가 (add)
        user.followers.add(request.user)
    return redirect('accounts:detail', pk)