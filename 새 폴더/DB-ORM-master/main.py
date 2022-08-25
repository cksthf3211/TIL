import sys
import os
import django
sys.dont_write_bytecode = True
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from db.models import *

# 아래에 코드를 기록하세요.
# 코드 실행은 터미널에서 shell을 실행시켜서 해주세요. 
# $ python manage.py shell_plus 

    # python -m venv venv
    # . venv/Scripts/activate
    # pip install -r requirements.txt
    # python manage.py --version

    # python manage.py makemigrations
    # python manage.py migrate

    # python manage.py shell_plus

# 4
p1 = Director.objects.get(name='봉준호')
print('id :',p1.id)
print('name :',p1.name)
print('debut :',p1.debut)
print('country :',p1.country)

# 5
p2 = Genre.objects.get(title = '드라마')
print('id:', p2.id )
print('title:', p2.title)

# 6  ༼ಢ  _ ಢ༽
d = Director.objects.get(name='봉준호')
g = Genre.objects.get(title='드라마')

m = Movie()
m.director = d
m.genre = g

m.title = '기생충'
m.opening_date = '2019-05-30'
m.running_time = '132'
m.screening = 'False'
 
m.save()

# 7 Movie 테이블 아래 데이터 추가
movies = [
    ("봉준호", "드라마", "괴물", "2006-07-27", 119, False),
    ("봉준호", "SF", "설국열차", "2013-10-30", 125, False),
    ("김한민", "사극", "한산", "2022-07-27", 129, True),
    ("최동훈", "SF", "외계+인", "2022-07-20", 142, False),
    ("이정재", "첩보", "헌트", "2022-08-10", 125, True),
    ("이경규", "액션", "복수혈전", "1992-10-10", 88, False),
    ("한재림", "재난", "비상선언", "2022-08-03", 140, True),
    ("Joseph Kosinski", "액션", "탑건 : 매버릭", "2022-06-22", 130, True),
]

for movies in Movie:   # 이게 맞나,,
    


# 8
Director object (1) Genre object (2) 기생충 2019-05-30 132 False
Director object (1) Genre object (2) 괴물 2006-07-27 119 False
Director object (1) Genre object (6) 설국열차 2013-10-30 125 False
Director object (2) Genre object (3) 한산 2022-07-27 129 True
Director object (3) Genre object (6) 외계+인 2022-07-20 142 False
Director object (4) Genre object (8) 헌트 2022-08-10 125 True
Director object (5) Genre object (1) 복수혈전 1992-10-10 88 False
Director object (6) Genre object (9) 비상선언 2022-08-03 140 True
Director object (7) Genre object (1) 탑건 : 매버릭 2022-06-22 130 True

# get은 하나의 값
# filter는 조건에만 맞으면 일종의 쿼리 리스트로 반환
