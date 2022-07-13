## CodeUp Python 기초 연습

```python
점심메뉴 = ['국밥','삼겹살','열라면','샐러드']
print(점심메뉴[0])
# 국밥이 출력됨
```

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

```python
#로또 1등 코드
import random
numbers = range(1, 46)
result = random.sample(numbers, 6)
print(result)
```

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



print(type(f))

git config user.email "cksthf321@gmail.com"

https://github.com/cksthf3211/TIL.git