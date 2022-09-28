from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'posts/index.html')

def new(request):
    return render(request, 'posts/new.html')

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    
    Posts.objects.create(title=title, content=content)
    
    context = {
        'title' : title,
        'content' : content,
    }
    return render(request, context)