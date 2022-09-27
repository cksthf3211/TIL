from django.shortcuts import render

from day3pjt.settings import BASE_DIR

# Create your views here.
def index(request):
    return render(request, 'index.html')

def ping(request):
    return render(request, 'ping.html')

def pong(request):
    # print(request)
    # print(dir(request))
    # print(request.get_full_path)
    # print((request.GET.get('ball'))
    name = request.GET.get('ball')
    context = { # 템플릿 안에서 뭐라고 칭할지
        'name' : name,
    }
    print(BASE_DIR)
    return render(request, 'pong.html', context)