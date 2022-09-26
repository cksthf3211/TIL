from locale import windows_locale
from django.shortcuts import render
import random

# Create your views here.
def is_odd_even(request, _number):
    num = _number
    if num == 0:
        check = 0
    elif num % 2 == 0:
        check = "짝수"
    else:
        check = "홀수"
    context = {
        "num": num,
        "check": check,
        }
    return render(request, "is_odd_even.html", context)

def calculate(request, _number1, _number2):
    num1 = _number1
    num2 = _number2
    
    context = {
        "num1" : num1,
        "num2" : num2,
        "add" : num1 + num2,
        "sub" : num1 - num2,
        "mul" : num1 * num2,
        "div" : num1 // num2,
    }
    return render(request, "calculate.html", context)

def form_(request):
    return render(request, "form_.html")
def form_2(request):
    nana = request.GET.get('ball')
    #print(request.GET)
    names = [
        "쥐", "말", "돼지", "노비", "동근님", "왕", "지렁이", "히틀러", "후세인", "스폰지밥", "은빈님",
    ]
    name = random.choice(names)
    context = {
        'name' : name,
        'nana' : nana,
    }
    return render(request, "form_2.html", context)


def lipsum(request):
     return render(request, "lipsum.html")

def lipsum_2(request):
    wowo = int(request.GET.get("wowo")) # 문단 수
    nono = int(request.GET.get("nono")) # 단어 수
    
    words = [
        "바나나", "딸기", "사과", "밤", "감", "도토리", "잣", "메론", "수박", "쌀",
    ]
    
    w_list = []
    for i in range(wowo): # 문단
        word_list = []
        for _ in range(nono): # 단어
            word = random.choice(words)
            word_list.append(word)
        print(word_list)
        w_list.append(word_list)
    print(w_list)
        
         
    context = {
        'word' : word,
        'wowo' : wowo,
        'nono' : nono,
        'w_list' : w_list
    }
    return render(request, "lipsum_2.html", context)