## Anaconda

Anaconda cmd 실행
conda --version

### 명령어

- conda env list
- conda activate
- conda deactivate
- conda --vesion

<!-- python 버전, 아나콘다 모듈 설치 -->

conda create -n PODO python

## VSCode

Ctrl + Shift + P 명령 팔레트
Python에서 Ananconda 가상환경 선택
Ctrl + Shift + `
test 실행하기

```python
print("hello")
print("안녕")
```

출력에 잘 나오는지 확인.

한글이 나오지 않는다면

1. 시스템 환경변수 편집
2. 고급 - 환경변수 - 시스템변수 - 새로 만들기 - PYTHONINCODING / utf-8

찾을 수 없다는 에러

- "ModuleNotFoundError: No module named 'PyQt5'"

오른쪽 상단 화살표 "Run Code" 말고 그 옆 작은 텝에 "Python 파일 실행" 눌러야함

## terminal

- pip install pyqt5
- pip install pyqt5-tools
- pip install matplotlib
- pip install numpy
- pip install psutil
- pip install pandas

- pip freeze > requirements.txt
- pip uninstall -r requirements.txt

## 기본

- 앱 크기: self.setGeometry(1100, 100, 700, 800)
- 종료버튼: btn.move(300, 720)

## 레이아웃(Layout)

- 레이아웃 (Layout)은 어플리케이션 창에 위젯들을 배치하는 방식
- 레이아웃 관리는 GUI 프로그래밍에서 매우 중요한 요소
- PyQt5의 위젯들을 배치하는 방식
  1. 절대적 배치
  2. 박스 레이아웃
  3. 그리드 레이아웃 방식
