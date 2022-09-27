from django.shortcuts import render
from day3pjt.settings import BASE_DIR
from .models.py import Article

# Create your views here.
def index(request):
    return render(request, 'index.html')

def index(request):
    guestbook = Article.object.all()
    return render(request, 'articles/index.html', {'guestbook': guestbook})


def create(request):
    content = request.GET.get('content')
    #questbook.append(content)
    # DB에 저장
    Article.objects.create(content=content)
    
    return render(request, 'articles/create.html', {'content': content})