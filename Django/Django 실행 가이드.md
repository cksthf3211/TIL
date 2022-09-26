# My Django Development Guide

1. 프로잭트 시작
2. vs코드 실행  ( ~ : home) ( . : 현재 파일)
3. 순서 시작
```bash
cd ~                             #home : 내pc c드라이브 - 사용자 - 내아이디폴더 ()

pwd                              # 프린트 워킹 디렉토리 (절대경로) /c/users/cksth

ls                               # list: 이것저것 나옴

mkdir server                     # server라는 폴더를 만듬

cd server/                       # server 폴더에 들어감

pip list                         # package와 version을 확인

python --version                 # python version 확인: Python 3.9.13

Python -m venv [가상환경이름]-venv    # 가상환경 생성

ls -a                            # 생성 확인

cd server-venv/                  # server-venv폴더에 들어감(가상환경을 유지하기 위한 파일이 들어있음)

ls                               # 목록 확인

cd ..                            # 한 칸 올라오기(이전 파일) 위치 주의 하기!!!

source test-venv/Scripts/activate # 가상환경 작동 (server-venv) 텝 으로 입력
                                 # 가상환경 안에서는 바깥에 영향을 미치지 않음
pip list                         # Django가 깔려있지 않은거 확인

---
deactivate                       # 가상환경 끄기
```
4. Django 설치
```bash
# 장고 설치
pip install  django==3.2.13      #Django 설치
# pip install  django 이건 가장 최신 버전 설치 ( 잘 안씀, 불안정함 )
pip install  django==3.2.12      #Django 설치

pip list                         # install 잘 되었는지 확인, Django 확인

pip --version                    # pip version 확인

django-admin startproject [프로젝트이름] [시작경로]  # firstpjt . ( .: 현재파일)

ls                               # project 확인

code .                           # project 코드를 열음, ls에서 확인된 폴더가 있음

python manage.py runserver       # 서버가 돌아가는 중

localhost:8000                   # 인터넷 주소창에 입력하여 서버가 잘 돌아가는지 확인

ctrl + c                         # 서버 종료
```

```bash
source [가상환경이름]-venv/Scripts/activate    # 가상환경 작동 후

python manage.py startapp [앱 이름]   # 앱 이름을 복수형으로 보자 (에러가 있음) articles
source [가상환경이름]-venv/Scripts/activate    # 가상환경 작동 후
pip list
```
- testpjt에 있는urls 파일 에 articles에 있는 views 파일 import
- articles에 있는 views testpjt에 있는urls 파일 index 함수를 정의

- articles 안에 templates 폴더를 만듬 ( 이름은 반드시 동일 )
-  templates 안에 index.html 만들고 ! 텝 하여 기본 구성

```bash
django-admin startproject [프로젝트이름] or django-admin startproject [프로젝트이름] . # 폴더 안 또는 현재 폴더에 프로젝트를 만듬
python manage.py startapp articles 
python manage.py runserver  # 서버를 돌림
localhost:8000              # 페이지를 찾을 수 없다
localhost:8000/index/
```

1. 가상환경 생성 실행
2. django LTS버전 설치
3. django 프로젝트 생성
4. 앱 생성
    1. 주의할 점: 커맨드를 manage.py가 있는 경로에서 실행
5. 앱 등록
    1. INSTALLED_APPS 에 프로젝트 파일명 입력
6. 서버 실행 테스트

```bash
black 설정
pip install black # Django 설치랑 같이 하기
```