from django.shortcuts import render
import random

# Create your views here.
def index(request):
    # 환영하는 메인 페이지를 보여준다.

    names = ['주세환', '오진수', '노은빈', '최근영', '홍길동', '박찬솔', '형', '하느']
    name = random.choice(names)
    context = {
        'name': name,
        'img':"https://cdn.crowdpic.net/detail-thumb/thumb_d_063DE2526E75F644AA2AE4BD774FE330.jpg",
    }

    return render(request, 'index.html', context)


def welcome(request, name):
    context = {
        'name' : name,
        'greetings' : [
            'hi', '안녕', '헤이',
        ],
        'images': [
            'https://shop3.daumcdn.net/thumb/R500x500/?fname=http%3A%2F%2Fshop3.daumcdn.net%2Fshophow%2Fp%2FR16378095882.jpg%3Fut%3D20220217041758',
            'https://image.yes24.com/goods/74271915/XL',
            'https://gongu.copyright.or.kr/gongu/wrt/cmmn/wrtFileImageView.do?wrtSn=13212706&thumbAt=Y&thumbSe=t_thumb&wrtTy=10004&filePath=L2Rpc2sxL25ld2RhdGEvMjAxOS8yMS9DTFMxMDAwNC8xMzIxMjcwNl9XUlQyMDE5MTAwOF8x',
        ],
    }
    # 사람들이 /welcome/본인이름을 입력하면, 환영인사와 이름을 동시에 보여준다.
    # print(name)
    return render(request, 'welcome.html', context)