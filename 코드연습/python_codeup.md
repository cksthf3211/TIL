# CodeUp Python 기초 연습
> [Python 기초 100제 (codeup.kr)](https://codeup.kr/problemsetsol.php?psid=33)

python 프로그래밍을 처음 배울 때 좋은 습관(단계)  
1. 입력된 문자열을 정확하게 잘라낸다
    - (공백, 줄바꿈, 구분문자 등에 따라 정확하게 잘라낸다.)  
3. 잘라낸 데이터들을 데이터형에 맞게 변환해 변수에 저장한다. 
    - (정수, 실수, 문자, 문자열 등에 따라 정확하게 변환한다.)  
5. 값을 저장했다가 다시 사용하기 위해, 변수를 이용해 값을 저장하고, 변수를 이용해 계산을 한다.  
6. 원하는 결과 값을 필요한 형태로 만들어 출력한다.(공백, 줄바꿈, 구분자, 등에 따라 원하는 형태로 만들어 출력한다.)

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
---
print(chr(ord(input())+1))
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
---
a, b = input().split()
print(int(a) - int(b))
```

```python
# 35번 - 실수 2개를 입력받아 곱을 출력하는 프로그램 출력 n
m = f1 * f2
print(m)
---
a, b = input().split()
print(float(a) * float(b))
```

```python
# 36번 - 단어 여러번 출력하기 n
w, n = input().split()
print(w*int(n))
```

```python
# 37번 - 문장 여러 번 출력하기
n = input()  
s = input()  
print(int(n)*s)
```

```python
# 38번 - 정수 2개 입력받아 거듭제곱 계산하기
c = a ** b
print(c)
---
a, b = input().split()
print(int(a) ** int(b))
```
```python
# 39번 - 실수 2개 입력받아 거듭제곱 계산
f1, f2 = input().split()
print(float(f1) ** float(f2))
```
```python
# 40번 - 정수 2개 입력받아 나눈 몫 계산
a, b = input().split()
print(int(a) // int(b))
```

## 41번~50번
```python
# 41번 - 정수 2개 입력받아 나눈 나머지 계산
a, b = input().split()
print(int(a) % int(b))
```
```python
# 42번 - 실수 1개를 입력받아 소숫점이하 자리 변환하기
a = float(input())
print(format(a,'.2f'))
```
```python
# 43번 - 실수 2개 입력받아 나눈 결과 계산
f1, f2 = float(input().split())
print(f1 // f2,'.3f')
---
a, b = map(float, input().split())
print('%.3f' %round((a / b), 3))
---
a, b = map(float, input().split())
c = a/b
print("%0.3f" % c)
---
a, b = input().split()
a = float(a)
b = float(b)
c = a/b
print('%.3f'%c)
```

```python
# 44번 - 정수 2개 입력받아 자동 계산
a, b = map(int, input().split())
# 합(+), 차(-), 곱(*), 몫(//), 나머지(%), 나눈 값(/)을 자동으로 계산
# 소수점 반올림을 해주는 round() 함수
print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)
print(round(a / b, 2))
```

```python
# 45번 - ## 정수 3개 입력받아 합과 평균 출력
a, b, c = map(int, input().split())
d = a + b + c
e = d / 3
print(d, round(e, 3))
---
a, b, c = map(int, input().split())
print((a+b+c), round((a+b+c)/3,2))
---
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
hap = a+b+c
avg = hap/3
print(hap, format(avg, ".2f"))
```

```python
# 46번 - 정수 1개 입력받아 2배 곱해 출력
a = int(input())
# 정수를 2배로 곱하거나 나누어 계산해 주는 비트단위시프트연산자 <<, >>를 이용
print(a << 1)
# 컴퓨터 내부에는 2진수 형태로 값들이 저장되기 때문에,  2진수 형태로 저장되어 있는 값들을 왼쪽(&lt;<)이나 오른쪽(&gt;>)으로 지정한 비트 수만큼 밀어주면 2배씩 늘어나거나 1/2로 줄어드는데, 왼쪽 비트시프트(<<)가 될 때에는 오른쪽에 0이 주어진 개수만큼 추가되고,  오른쪽 비트시프트(>>)가 될 때에는 왼쪽에 0(0 또는 양의 정수인 경우)이나 1(음의 정수인 경우)이 개수만큼 추가되고, 가장 오른쪽에 있는 1비트는 사라진다.
# print(n<<1)  #10을 2배 한 값인 20 이 출력
# print(n>>1)  #10을 반으로 나눈 값인 5 가 출력
# print(n<<2)  #10을 4배 한 값인 40 이 출력
# print(n>>2)  #10을 반으로 나눈 후 다시 반으로 나눈 값인 2 가 출력
```

```python
# 47번 - 2의 거듭제곱 배로 곱해 출력
a, b = map(int, input().split())
print(a << b)
# a = 2  
# b = 10  
# print(a << b)  #2<sup>10</sup> = 1024 가 출력된다.
```

```python
# 48번 - 정수 2개 입력받아 비교
a, b = map(int, input().split())
# a가 b보다 작은 경우 True 를, 그렇지 않은 경우 False 를 출력
a, b = map(int, input().split())
if a < b:
    print('True')
else:
    print('False')
```

```python
# 49번 - 정수 2개 입력받아 비교
a, b = map(int, input().split())
if a == b:
    print("True")
else:
    print('False')
```

```python
# 50번 - 정수 2개 입력받아 비교
a, b = map(int, input().split())
if a <= b:
    print('True')
else:
    print('False')
```
## 51번~60번

```python
# 51번 - 정수 2개 입력받아 비교
a, b = map(int, input().split())
if a != b:
    print("True")
else:
    print("False")
```
```python
# 52번 - 정수 입력받아 참 거짓 평가
n = int(input())  
print(bool(n))
```
```python
# 53번 - 참 거짓 바꾸기
a = bool(int(input()))
# 위는 input( ), int( ), bool( ) 순서로 한 번에 한 단계씩 계산/처리/평가
print(not a)
```
```python
# 54번 - 둘 다 참일 경우만 참 출력
a, b = input().split()
# and 예약어는 주어진 두 불 값이 모두 True 일 때에만 True 로 계산하고, 나머지 경우는 False
print(bool(int(a)) and bool(int(b)))
---
a, b = map(int, input().split())
print(bool(a) and bool(b))
```
```python
# 55번 - 하나라도 참이면 참 출력
a, b = map(int, input().split())
print(bool(a) or bool(b))
```
```python
# 56번 - 참/거짓이 서로 다를 때에만 참 출력
a, b = map(int, input().split())
c = bool(a) # True
d = bool(b)  # True
print((c and (not d)) or ((not c) and d))
# c and (not d)는 c가 True일 때, d는 False = False
# (not c) and d는 c가 False일 때, d는 True = False
# a, b 둘다 참이기 때문에 False 출력
---
a, b = map(int, input().split())
if (bool(a) ^ bool(b) == True):
    print("True")
else:
    print("False")
```
```python
# 57번 - 참/거짓이 서로 같을 때에만 참 출력
a, b = map(int, input().split())
c = bool(a) # False
d = bool(b) # False
print(a==b)
---
a, b = map(int, input().split())
if (bool(a) ^ bool(b) == True):
    print("False")
else:
    print("True")
```
```python
# 58번 - 둘 다 거짓일 경우만 참 출력
a, b = map(int, input().split())
c = bool(a) # False
d = bool(b) # False
print(not (c or d))
---
a, b = map(int, input().split())
if ((bool(a)) ^ (bool(b)) == True):
    print('False')
else:
    print('True')
---
a, b = map(int, input().split())
a, b = bool(a), bool(b)

if (a == False and b == False):
    print("True")
else:
    print("False")
```
```python
# 59번 - 비트단위로 NOT 하여 출력
# ~ (bitwise not)
# & (bitwise and)
# | (bitwise or)
# ^ (bitwise xor),  
# << (bitwise left shift)
# >> (bitwise right shift)
n = int(input())
print(~~n)
```
```python
# 60번 - 비트단위로 AND 하여 출력
a, b = map(int, input().split())
# &(엠퍼센드)는 둘 다 1인 부분의 자리만 1로 만들어주는 것과 같다
print(a&b)
```

## 61번~70번
```python
# 61번 - 비트단위로 OR 하여 출력
# | 은 파이프(pipe)연산자
a, b = map(int, input().split())
# or 연산은 둘 중 하나라도 1인 자리를 1로 만들어주는 것과 같다
print(a | b)
```
```python
# 62번 - 비트단위로 XOR 하여 출력
a, b = map(int, input().split())
print(a ^ b)
```
```python
# 63번 - 정수 2개 입력받아 큰 값 출력
a, b = map(int, input().split())
print( a if (a > b) else b)
```
```python
# 64번 - 정수 3개 입력받아 가장 작은 값 출력
a, b, c = map(int, input().split())
d = a if a < b else c
print(d if d < c else c)
---
a, b, c = map(int, input().split())
result = (a if a < b else b) if a < c else (c if c < b else b)
print(result)
---(여기서 띠용 했음)
a, b, c = map(int, input().split())
print(min(a,b,c))
---
a, b, c = map(int, input().split())
d = a if a < b else b
e = d if d < c else c

print(e)
```
```python
# 65번 - 정수 3개 입력받아 짝수만 출력
a, b, c = map(int, input().split())
if a % 2 == 0:
    print(a)
if b % 2 == 0:
    print(b)
if c % 2 == 0:
    print(c)
---
print(*(filter(lambda x: not x % 2, [a, b, c])))
```
```python
# 66번 - 정수 3개 입력받아 짝/홀 출력
a, b, c = map(int, input().split())
if a % 2 == 0:
    print('짝')
else:
    print('홀')
if b % 2 == 0:
    print('짝')
else:
    print('홀')
if c % 2 == 0:
    print('짝')
else:
    print('홀')
---
print(*map(lambda num: 'even' if not num % 2 else 'odd', [a, b, c]))
```
```python
# 67번 - 정수 1개 입력받아 분류
# 음수이면서 짝수이면, A  
# 음수이면서 홀수이면, B  
# 양수이면서 짝수이면, C  
# 양수이면서 홀수이면, D
n = int(input())
if n < 0:
    if n % 2 == 0:
        print('A')
    elst:
        print('B')
if n > 0:
    if n % 2 == 0:
        print('C')
    else:
        print('D')
```
```python
# 68번 - 점수 입력받아 평가 출력
# 90 ~ 100 :A  
# 70 ~ 89 : B  
# 40 ~ 69 : C  
# 0 ~ 39 :  D
n = int(input())
if n  >= 90:
    print('A')
else:
    if n >= 70:
        print('B')
    else:
        if n >= 40:
            print('C')
        else:
            print('D')
---
n = int(input())
if n  >= 90:
    print('A')
elif n >= 70:
    print('B')
elif n >= 40:
    print('C')
else:
    print('D')
# elif 를 사용하면 if ... else ... 구조를 겹쳐 사용할 때처럼, 여러 번 안 쪽으로 들여쓰기 하지 않아도 된다.
# elif는 else if 의 짧은 약어
```
```python
# 69번 - 평가 입력받아 다르게 출력
# A = best!!!
# B = good!!
# C = run!
# D = slowly~
# E = what?
chr = input()
if chr  == 'A':
    print('best!!!')
elif chr == 'B':
    print('good!!')
elif chr == 'C':
    print('run!')
elif chr == 'D':
    print('slowly~')
else:
    print('what?')
```
```python
# 70번 - 월 입력받아 계절 출력
# 월이 입력될 때 계절 이름이 출력
---( 틀림 )
n = int(input())
if n // 3 == 1:
    print("spring")
elif n // 6 == 1:
    print('summer')
elif n // 9 == 1:
    print('winter')
else:
    print('fall')
---( 틀림 )
n = int(input())
if n // 3 == 1:
    print("spring")
else:
    if n // 6 == 1:
        print('summer')
    else:
        if n // 9 == 1:
            print('winter')
        else:
            print('fall')
---( 풀이 )
n = int(input())

if a == 12 or a == 1 or a == 2:
    print("winter")
elif a == 3 or a == 4 or a == 5:
    print("spring")
elif a == 6 or a == 7 or a == 8:
    print("summer")
elif a == 9 or a == 10 or a == 11:
    print("fall")
```

## 71번~80번
```python
# 71번 - 0 입력될 때까지 무한 출력
n = 1
while n != 0:
    n = int(input())
    if n != 0:
        print(n)
```
```python
# 72번 - 정수 1개 입력받아 카운트다운 출력1
n = int(input())

while n!=0:   # n가 0이 아니라면
    print(n)  # n 출력
    n = n - 1 # n가 1씩 감소 - 결과적으로 0이 되면 출력하지 않음
```
```python
# 73번 - 정수 1개 입력받아 카운트다운 출력2
n = int(input())
    
while n != 0:
    n -= 1   # 5라고 가정하면 4 출력
    print(n) # 1이라고 가정하면 0출력으로 종료 
```
```python
# 74번 - 문자 1개 입력받아 알파벳 출력
c = ord(input())     # c = 입력받을 문자
t = ord('a')         # t = a부터
while t <= c:        # a부터 입력받은 문자가 같거나 클때까지
    print(chr(t), end = '')  # a부터 출력
    t += 1                   # 하나씩 커짐(아스키 코드 65)
```
```python
# 75번 - 정수 1개 입력받아 그 수까지 출력
n = int(input())
a = int(0)
while a <= n:
    print(a, end = '\n')
    n += 1
```
```python
# 76번 - 정수 1개 입력받아 그 수까지 출력
n = int(input())
for i in range(n+1): # range(n)에 들어있는(in) 각각의 수에 대해서(for) 순서대로 i에 저장
    print(i)
```
```python
# 77번 - 짝수 합 구하기
n = int(input())  # 6
s = 0
for i in range(1, n+1) :
  if i%2==0:      # 2 4 6
    s += i
   
print(s)          # 12
---(While문으로 작성하기 연습)
n = int(input())
n1 = 0
sum = 0
while n1 <= n:
    sum = sum + n1
    n1 = n1 + 2
print(sum)
```
```python
# 78번 - 원하는 문자가 입력될 때까지 반복 출력
while True:       # 조건이 True면 밑에 내용 실행
    x = input()   # x가 input()으로 주어짐
    print(x)      # 조건이 참이면 주어진 input을 실행
    if x == 'q':  # 주어진 input이 q를 만나게 된다면
        break     # break 멈춤 실행
---
word = ""          # 입력 값을 n 변수 지정
while word != "q": # while문을 사용해서 "word가 "q"와 같지 않을 때만 반복실행
    word = input() # while문이 시작되면 input()을 받아서 word에 넣는다
    print(word)    # word가 출력되다가 "q"를 입력받으면 while문은 종료
```
```python
# 79번 - 언제까지 더해야 할까?
n = int(input())    # 정수를 받아옴
s = 0               # 더할 값 
t = 0               # 시작 값
    while s < n:    # s가 n보다 같거나 작을 때
        t = t + 1   # 시작값이 1씩 커짐  - 1 (0부터 시작이니까)
        s = s + t   # 시작값 + 1 ~ n까지 순서대로 더함
print(t)            # 주어진 n보다 s가 작을 때 까지 시작값에 1씩 더한 것을 출력
---
n = int(input())   # 정수를 받아옴
a = 1              # 1부터 더하고 출력 할 시작 값
b = 1
while True:        # 조건이 참이면 실행
    if a < n:      # a가 n보다 같거나 작을때까지
        b = b + 1
        a = a + b  # 1는 다음 숫자를 하나씩 더함
print(b)
```
```python
# 80번 - 주사위 2개 던지기
n, m= map(int,input().split())
for i in range(1, n+1) :
    for j in range(1, m+1) :
        print(i, j)
```

## 81번~90번
```python
# 81번 - 16진수 구구단 출력
n = int(input(), 16)
for i in range(1, 16):
    print('%X' %n, '*%X' %i, '=%X' %(n*i), sep='')
---
a = int(input(), 16) 
for i in range(1, 16):
    print(("%X" % a) + '*' \+ ('%X' % i) + '=' \+ ('%X' % (a*i)))
```
```python
# 82번 - 3 6 9 게임의 왕이 되자
# 몫(//), 나머지(%), 나눈 값(/)
a = int(input())

for i in range(1, a+1):

    if i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
        print('X', end = ' ')
    else:
        print(i, end = ' ')
```
```python
# 83번 - 빛 섞어 색 만들기
r, g, b = map(int, input().split())
cnt = 0
for i in range(r):
    for j in range(g):
        for k in range(b):
            cnt += 1
            
            print(i,j,k)
print(c)
```
```python
# 84번 - 소리 파일 저장용량 계산
# 1초 동안 마이크로 소리강약을 체크하는 횟수를 h
# 한 번 체크한 값을 저장할 때 사용하는 비트수를 b
# 좌우 등 소리를 저장할 트랙 개수인 채널 개수를 c
# 녹음할 시간(초) s
# 소수점 첫째 자리까지의 정확도로 출력하고 MB를 공백을 두고 출력
h, b, c, s = map(int, input().split())

f = (h *b * c * s / 8 / 1024 / 1024)
a = round(f,1)
print(f'{a} MB')
```
```python
# 85번 - 그림 파일 저장용량 계산
# 이미지의 가로 해상도 w, 세로 해상도 h, 한 픽셀을 저장하기 위한 비트 b
w, h, b = map(int, input().split())

f = (w * h * b / 8 / 1024 / 1024)
a = round(f,2)
print(f'{a} MB')
---
a,b,c=input().split()

W=int(a)
H=int(b)
B=int(c)

print('%.2f MB' % (W\*H\*B/8/1024/1024))
```
```python
# 86번 - 거기까지! 이제 그만~
n = int(input())
s = 0
c = 0
while True:
    s += c
    c += 1
    if n <= s:
        break
print(s)
```
```python
# 87번 - 3의 배수는 통과
n = int(input())

for i in range(1,n+1):
    if i % 3 == 0:
        continue             # #다음 반복 단계로 넘어간다.
    else:
        print(i, end = ' ')
# continue 가 실행되면, 반복 블록 안에 있는 나머지 부분을 실행하지 않고, 다음 반복 단계로 넘어간다.  
# 즉, 반복 블록의 나머지 부분은 실행되지 않고, 다음 단계의 반복을 계속(continue)하는 것
```
```python
# 88번 - 수 나열하기1
# 규칙에 따라 수를 순서대로 나열한 것을 수열(sequences)
# 시작 값(a), 등차(d), 몇 번째인지(n)
# n번째 수를 출력하는 프로그램
a, d, n = map(int, input().split())

for i in range(n - 1): # 0, 1, 2, 3, 4
    a = a + d
    print(a)
---
a,d,n=map(int, input().split())
print(a+d*(n-1))
```
```python
# 89번 - 수 나열하기2
a, r, n = map(int, input().split())
for i in range(n-1):
    a = a * r
    print(a)
---
a, r, n = map(int, input().split()) # 2 3 7
list = []
for i in range(n-1):
    a = a * r
    list.append(a)
print(max(list))
```
```python
# 90번 - 수 나열하기3
# 시작 값(a), 곱할 값(m), 더할 값(d), 몇 번째인지(n)
a, m, d, n = map(int, input().split())
for i in range(n - 1):
    a = a * m + d
    c.append(a)
    p = c.pop()
print(p)
---
a,m,d,n = map(int,input().split())

for i in range(1,n):
    a = (m*a)+d
print(a)
```

## 91번~100번
```python
# 91번 - 함께 문제 푸는 날, 최소공배수
# 3명이 같은 날 가입/등업하고, 각각 3일마다, 7일마다, 9일마다 한 번씩 들어온다면, 처음 가입하고 63일 만에 다시 3명이 함께 문제를 풀게 된다.
# 
a, b, c = map(int, input().split()) # 3 7 9
d = 1
while d % a != 0 or d % b != 0 or d % c != 0 :
    d += 1
print(d)
---
import math
a, b, c = map(int, input().split())
d = math.lcm(a, b, c) # 최소 공배수
print(d)
---
import math   
math.gcd(A, B)  # 최대 공약수
```
```python
# 92번 - 이상한 출석 번호 부르기1
# 무작위(랜덤)
n = int(input())         # 10
a = input().split()      # 1 3 2 2 5 6 7 4 5 9

for i in range(n) :      # 0 ~ 9
  a[i] = int(a[i])       # [a]

d = []
for i in range(24) :     # 0~23
  d.append(0)            # [0, 0, ... , 0, 0, 0] 24개

for i in range(n) :      # 0~9
  d[a[i]] += 1           #번호를 부를 때마다, 그 번호에 대한 카운트 1씩 증가

for i in range(1, 24) :  #카운트한 값을 공백을 두고 출력
  print(d[i], end=' ')
```
```python
# 93번 - 이상한 출석 번호 부르기2
num = int(input())
numlist = input().split()

numlist.reverse()

for i in range(0,num):
    print(numlist[i], end=' ')
```
```python
# 94번 - 이상한 출석 번호 부르기3
n = int(input())
k = map(int,input().split())

a = min(k)
print(a)
```
```python
# 95번 - 바둑판에 흰 돌 놓기
# 바둑판(19 * 19)
# n개의 흰 돌이 놓인 위치를 출력하는 프로그램을 작성
# 바둑판에 올려 놓을 흰 돌의 개수(n)가 첫 줄에 입력
# 둘째 줄 부터 n+1 번째 줄까지 힌 돌을 놓을 좌표(x, y)가 n줄 입력
# x, y 좌표는 1 ~ 19
# 흰 돌이 올려진 바둑판의 상황을 출력
# 흰 돌이 있는 위치는 1, 없는 곳은 0으로 출력
m = []

for i in range(20):
    m.append([])         # 리스트 안에 다른 리스트 추가해 넣기
    for j in range(20):
        m[i].append(0)   # 리스트 안에 들어있는 리스트 안에 0 추가해 넣기
    
n = int(input())         # 5

for i in range(n):      
    x, y = map(int, input().split()) # 좌표
    m[x][y] = 1 # 좌표가 있는 곳은 리스트에서 1로 표시

for i in range(1, 20):
    for j in range(1, 20):
        print(m[i][j], end = ' ')
    print()             # 줄 바꿈
```

```python
# 96번 - 바둑알 십자 뒤집기
# 길이가 다른 몇 개의 막대를 바둑판과 같은 격자판
# 막대에 있는 설탕과자 이름 아래에 있는 번호를 뽑으면 설탕과자를 가져가는 게임
# 격자판의 세로(h), 가로(w), 막대의 개수(n), 각 막대의 길이(l),  
# 막대를 놓는 방향(d:가로는 0, 세로는 1)과  
# 막대를 놓는 막대의 가장 왼쪽 또는 위쪽의 위치(x, y)가 주어질 때,  
# 격자판을 채운 막대의 모양을 출력하는 프로그램을 만들어보자
location = []

for i in range(19):
    location.append([])

    for j in range(19):
        location[i].append(0)

for i in range(19):
    location[i] = list(map(int, input().split()))

n = int(input())

for i in range(n):
    x, y = map(int, input().split())

    for j in range(19):
        if location[x-1][j] == 0:
            location[x-1][j] = 1
        else:
            location[x-1][j] = 0
        if location[j][y-1] == 0:
            location[j][y-1] = 1
        else:
            location[j][y-1] = 0

for i in range(19):
    for j in range(19):
        print(location[i][j], end=" ")
        
    print()
```
```python
# 97번 - 설탕과자 뽑기
h, w = map(int, input().split())
n = int(input())

zeros = [[0] * w for _ in range(h)]

for i in range(n):
    l, d, x, y = map(int, input().split())

    for j in range(l):
        if d == 0:
            zeros[x-1][y-1+j] = 1
        else:
            zeros[x-1+j][y-1] = 1

for i in range(h):
    for j in range(w):
        print(zeros[i][j], end=' ')
    print()
```
```python
# 98번 - 성실한 개미
array = []

for i in range(10):
    array.append(list(map(int, input().split())))

x, y = 1, 1

while True:
    if (array[x][y] == 0):
        array[x][y] = 9
    elif (array[x][y] == 2):
        array[x][y] = 9
        break

    if ((array[x][y+1] == 1 and array[x+1][y] == 1)):
        break

    if (array[x][y+1] != 1):
        y = y + 1
    elif (array[x+1][y] != 1):
        x = x + 1

for i in range(10):
    for j in range(10):
        print(array[i][j], end=' ')
    print()
```

## Review





