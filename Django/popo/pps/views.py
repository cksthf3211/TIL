from django.shortcuts import redirect, render
from .models import Article

# Create your views here.

def index(request):
    return render(request, 'pps/index.html')

def new(request):
    return render(request, 'pps/new.html')

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    Article.objects.create(title=title, content=content)
    return redirect('pps:index')