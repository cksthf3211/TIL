import re
from urllib import request  # 이거 언제 생겻지
from django.shortcuts import render
import random

# Create your views here.

def index(request):

    menus = [
        {"menu" : '곱창', "src" : "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSestD2DTLhMcaajy58n3Y68jUUjK6F58MXF0Q5Di2eEikD2mDi6HUZLy7Du0pPfldQYgU&usqp=CAU"},
        {"menu" : '피자' , "src" : "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSn-TolvVY2xhx7qQlkSFaCh1qEjqog3Z1U4w&usqp=CAU"},
        {"menu" : '햄버거' , "src" : "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTHI_UvRiKSgtAHAOnxe1HjET2ur5BQf9mV7Q&usqp=CAU"},
        {"menu" : '삼겹살' , "src" : "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR5EPQG-WCeSDhCm692AiMfADd5tSEqo3LL4g&usqp=CAU"},
        {"menu" : '소갈비살' , "src" : "http://gdimg.gmarket.co.kr/1783317825/still/600?ver=1639024220"},
        {"menu" : '치킨' , "src" : "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR4zrRYDpWroSUMYfXIK4FWgmDAuDf9I7I9KQ&usqp=CAU"},
        {"menu" : '순대국밥' , "src" : "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTROnES8e0rQM5EOqceUikG7dQJ2-Pg4KHw3g&usqp=CAU"},
        {"menu" : '초밥' , "src" : "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT3W5zpWBvZKaVjsGk9PShL1XxJyrW--yOaag&usqp=CAU"},
        {"menu" : '돈까스' , "src" : "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSyMfz99Vv378Qi7tvipLrZzcrfwA_tPP1dcg&usqp=CAU"},
        {"menu" : '제육볶음' , "src" : "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ5Kn9e21mPIvLvOp6oshH9GzwhEWjUTPVlsg&usqp=CAU"},
        {"menu" : '낚지볶음' , "src" : "http://th2.tmon.kr/thumbs/image/a93/82d/f98/eec380d2b_700x700_95_FIT.jpg"},
        {"menu" : '편의점황제투어' , "src" : "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTj6JjX4hJ6_nBswCOkKxv2OhvtVk0JLnBUyQ&usqp=CAU"},
        ]

    menu = random.choice(menus)
    context = {
        'menu' : menu,
    }

    return render(request, 'index.html', context)


# def Lotto(request):
#     numbers = [ 1, 45 ]
#     number = random.choice(numbers)
#     context = {
#         'number' : number
#     }
#     return render(request, 'Lotto.html', context)


def index(request):
    return render(request, "index.html")


def today_beer(request):
    beer_list = [
        {"name": "에델바이스", "src":""},
        {"name": "에델바이스", "src":""},
        {"name": "에델바이스", "src":""},
        {"name": "에델바이스", "src":""},
        {"name": "에델바이스", "src":""},
        {"name": "에델바이스", "src":""},
    ]

    context = {
        "beer_list" : random.choice(beer_list)
    }
    return render(request, "today_beer.html", context)


# ---


def lotto(request):
    # 로또 번호 6개를 5번 뽑기
    # lotto_result_list = [
    #     {"lotto": [1, 2, 3, 4, 5, 6], "result" : "1등 - 10억"},
    #     {"lotto": [1, 2, 3, 4, 5, 6], "result" : "1등 - 10억"},
    #     {"lotto": [1, 2, 3, 4, 5, 6], "result" : "1등 - 10억"},
    #     {"lotto": [1, 2, 3, 4, 5, 6], "result" : "1등 - 10억"},
    #     {"lotto": [1, 2, 3, 4, 5, 6], "result" : "1등 - 10억"},
    # ]

    lotto_list = []
    for _ in range(5):
        lotto = random.sample(range[1,46],6)
        lotto_list.append(lotto)

    context = {
        "lotto" : lotto,
    }
    return render(request, "lotto.html", context)


# ---
def LottoT(request):
    return render(request,'LottoT.html')

def LottoC(request):
    num = int(request.GET.get('num'))
    Lottos = []
    for data in range(num):
        Lottos.append(random.sample(range(1, 46),6))

    context = {
        'num' : num,
        'Lottos' : Lottos,
    }
    return render(request,'LottoC.html',context)