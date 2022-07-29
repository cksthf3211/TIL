# CodeUp Python 기초 연습
> [Python 기초 100제 (codeup.kr)](https://codeup.kr/problemsetsol.php?psid=33)
### 연습
```python
점심메뉴 = ['국밥','삼겹살','열라면','샐러드']
print(점심메뉴[0])
# 국밥이 출력됨
```
```python
#로또 1등 코드
import random
numbers = range(1, 46)
result = random.sample(numbers, 6)
print(result)
```
```python
#구구단
for i in range(2, 10):
    for j in range(1, 10):
        print(i*j, end =" ")
    print()
```
## 1~10번
```python
#1번 - 문장
print('Hello')
# Hello 출력
```

```python
#2번 - 문장열
print("Hello", "World")
# Hello World 출력
```

```python
#3번 - 줄바꿈
print("Hello") 
print("World")
# Hello
# World
```

```python
#4번 - 작은따옴표
print("'Hello'")
# 'Hello'출력
```

```python
#5번 - 큰따옴표
print('"Hello World"')
# "Hello World" 출력
```

```python
#6번 - 특수문자
print("\"\"!@#$%^&*()'\"\)
#\" 또는 \' 를 이용하여 출력할 수 있다.
# "!@#$%^&*()' 출력
```

```python
#7번 - 파일 경로 출력

print('\"C:\\Download\\\'hello\'.py\"')
'\\\\\\'
# "C:\Download\'hello'.py" 출력
```

```python
#8번 - 역슬레쉬 출력
print("Hello\nWorld")
위 코드를 정확히 그대로 출력하시오.
print("print(\"Hello\\nWorld\")")
# print("Hello\nWorld") 출력
```

```python
#9번 - 문자 1개 그대로 출력
a = input()
print("a")
# a 출력
```

```python
#10번 - 숫자 1개를 그대로 출력 (숫자x)
#input은 문자. 숫자로 바꾸려면 int(정수)
a = input(15)
b = int(a)
print(b)
#또는
num = input()
num = int(15)
print(int, type(num))
#또는
a = input()
b = int(15)
print(b)
#또는
num = input()
print(int, type(num))
#또는
a = input(a)
a = int(a)
print(a)
```

## 11번~20번
```python
# 11번 - 소수점 1.414213
f = input()
f = float(f)
print(type(f))
#또는
a = input()
a = float(a)
print(a)
```

```python
# 12번 - 줄을 바꿔 정수 2개를 입력받아 출력
a = input()
b = input()
print(a)
print(b)
```

```python
# 13번 - 줄을 바꿔 문자2개 입력받고 순서를 바꿔 한 줄씩 출력
a = input()
b = input()
print(b)
print(a)
```

```python
# 14번 - 실수 1개를 입력받아 줄을 바꿔 3번 출력
a = input()
a = float(a)
print(a)
print(a)
print(a)
```

```python
# 15번 - 공백을 두고 입력된 정수 2개를 입력받아 줄을 바꿔 출력
a,b = input().split()
#split을 사용하면 공백을 기준으로 입력된 값들을 나누어 자른다.
a = int(a)
b = int(b)
print(a)
print(b)
```

```python
# 16번 - 공백을 두고 문자 2개를 입력받아 순서를 바꿔 출력해보자
a, b = input().split()
print(b, a)
#핵심은 split()이다. 스플릿 안에 공백이면 공백을 기준으로 나눈다.
```

```python
# 17번 - 정수, 실수, 문자, 문자열 등 1개만 입력받아 한 줄로 3번 출력해보자
s = input()
print(s, s, s)
#python 언어에서는 문자/정수/실수/문자열 등 특별한 구분이 없이도 원하는 변수에 저장시켜 출력 할 수 있다.
#하지만, 저장된 값을 이용해 계산하거나 서로 붙여 연결시키거나 잘라내는 작업을 한다면?
#반드시 저장되어있는 값의 종류(문자/정수/실수/문자열 등)를 구분해 주어야 한다.
```

```python
# 18번 - 24시간 시:분 형식으로 시간이 입력될 때, 그대로 출력하는 연습을 해보자
a, b = input().split(':')
print(a, b, sep=':')
#input().split(':') 를 사용하면 콜론 ':' 기호를 기준으로 자른다.
#print(a, b, sep=':') 를 사용하면 콜론 ':' 기호를 사이에 두고 값을 출력한다.
#sep 는 분류기호(seperator)를 의미한다.
```

```python
# 19번 - "연도.월.일"을 입력받아 "일-월-연도" 순서로 바꿔 출력해보자
#y, m, d = input().split('.')과 같이 변수들을 순서대로 나열하면 구분기호를 기준으로 잘라 순서대로 저장
y, m, d = input().split('.')
print(d,m,y, sep='-')
#sep='' 는 여러개를 동시에 출력할 때 구분값
```

```python
# 20번 - 주민번호 출력하기
# 주민번호 앞 6자리와 뒷 7자리가 '-'로 구분되어 입력된다.
# -'를 제외한 주민번호 13자리를 모두 붙여 출력한다.
# 아무것도 없는 공(empty) 문자는 작은 따옴표 (') 2개를 붙여서 '' 로 표현한다.
# input 000907-1121112
#output 0009071121112
a,b = input().split('-')
print(a+b)
```

## 21번~30번
```python
# 21번 - 띄워서 출력하기
# 알파벳과 숫자로 이루어진 단어 1개가 입력된다.
#입력받은 단어의 각 문자를 한 줄에 한 문자씩 분리해 출력한다
# input = Hello
s = input()
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])
```

```python
# 22번 - 6자리 YYMMDD을 입력받아 나누어 출력
# 를 실행하면 0번째 문자부터 1번째 문자까지 잘라 출력한다.
# s[a:b] 라고 하면, s라는 단어에서 a번째 문자부터 b-1번째 문자까지 잘라낸 부분을 의미한다.
#년도(YY) 월(MM) 일(DD)을 공백으로 구분해 한 줄로 출력한다.
# input = 200304 output = 20 03 04
s = input()
print(s[0:2], s[2:4], s[4:6])
```

```python
# 23번 - 시:분:초 에서 분 출력
# 시:분:초 형식으로 시간이 입력될 때 분만 출력
# 어떻게 분만 출력해야 할지 주의 깊게 생각
#input = 17:23:57
h, m, s = input().split(':')
print(m)
```

```python
# 24번 - 단어 2개를 입력받아 이어붙이기
# 단어는 문자(character)
# 문자들로 구성된 문장을 문자열(string)
# 문자열에는 공백문자(' ')가 포함될 수 있는데, 문자 1개는 길이가 1인 문자열이라고 할 수 있고, 공백문자(' ')가 없는 문자열은 단어(word)라고 할 수 있다.
# input = Hellow World
w1, w2 = input().split(' ')
s = w1 + w2
print(s)
# 이건 틀림.. 왜,,? 스플릿이 공백을 잘라서?
w1, w2 = input()
s = w1 + w2
print(s)
```

```python
# 25번 - 정수 2개를 입력받아 합 계산하기
# 입력되는 값은 기본적으로 문자열로 인식
#문자열 + 문자열은 두 문자열을 합친 문자열을 만든다.
# 숫자로 구성된 문자열이나 실수를 정수(integer) 값으로 바꾸기 위해서는 int( ) 를 사용
# 수 + 수의 결과는 합(addition)이 계산된다.
# 2개의 정수가 공백으로 구분되어 입력
# input = 123
a, b = input().split(' ')
c = int(a) + int(b)
print(c)
```

```python
# 26번 - 실수 2개를 입력받아 합 계산하기
# 숫자로 구성된 문자열이나 정수를 실수(real number) 값으로 바꾸기 위해서는 float( ) 를 사용할 수 있다.
# 소숫점(.)은 그 위치가 정해져있지 않고 이리저리 둥둥 떠다니므로, floating point라고 부른다.
# input 0.1, 0.9 줄 바꿔 입력
a = input()
b = input()
c = float(a) + float(b)
print(c)

```

```python
# 27번 - 10진 정수 16진수로 출력
# 10진수 형태로 입력받고 %x로 출력하면 16진수(hexadecimal) 소문자로 출력된다.
# (%o로 출력하면 8진수(octal) 문자열로 출력된다.)
# 10진법은 한 자리에 10개(0 1 2 3 4 5 6 7 8 9)의 문자를 사용하고, 16진법은 영문 소문자를 사용하는 경우에 한 자리에 16개(0 1 2 3 4 5 6 7 8 9 a b c d e f)의 문자를 사용한다.
#16진수 a는 10진수의 10, b는 11, c는 12 ... 와 같다.
# input = 255 output f
a = input()
n = int(a)
print('%x'% n)
```

```python
# 28번 - 10진 정수 16진수로 출력
a = input()
n = int(a)
print('%X'% n)
```

```python
# 29번 - 16진수를 8진수로 출력
# input = f output = 17
a = input()
n = int(a,16)
print('%o'%n)
```

```python
# 30번 - 영문자 1개를 10진수로 변환
# ord( ) 는 어떤 문자의 순서 위치(ordinal position) 값을 의미한다.
n = ord(input())
print(n)
```
## 31번~40번
```python
# 31번 - 정수로 입력받아 유니코드 문자로 출력
# print(chr(c))  #c에 저장되어 있는 정수 값을 유니코드 문자(chracter)로 바꿔 출력한다. 
c = int(input())
print(chr(c))
```

```python
# 32번 - 정수 1개를 입력받아 부호 바꾸기
n = int(input())
print(-n)
```

```python
# 33번 - 문자 1개를 입력받아 그 다음 문자 출력
c = ord(input())
print(chr(c+1))
```

```python
# 34번 - 정수 2개를 입력받아 차 계산하기
c = input(a) - input(b)
print(c)
#
a = input()
b = input()
c = a - b
print(c)
```

```python
# 35번 - 실수 2개를 입력받아 곱을 출력하는 프로그램 출력 n
m = f1 * f2
print(m)
```

```python
# 36번 - 단어 여러번 출력하기 n
# 
w, n = input().split()
print(w*int(n))
```

```python
# 37번 - 
# 
```



a
print(type(f))

git config user.email "cksthf321@gmail.com"

https://github.com/cksthf3211/TIL.git

