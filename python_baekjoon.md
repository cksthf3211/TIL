# BAEKJOON
> [Baekjoon Online Judge (acmicpc.net)](https://www.acmicpc.net/)
```python
# 1000번
A, B = map(int, input().split())
print(A+B)
```
```python
# 2558번
A = int(input())
B = int(input())
print( A + B )
```
```python
# 10950번
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다.
# 각 테스트 케이스마다 A+B를 출력
T = int(input())
for i in range(T):
    A, B = map(int, input().split())
    print(A + B)
```
```python
# 10953번
# 각 테스트 케이스는 , 로 구분
T = int(input())
for i in range(T):
    A, B = map(int, input().split(','))
    print(A + B)
```
```python
# 11021번
# 각 테스트 케이스마다 "Case #x: "를 출력한 다음, A+B를 출력한다. 테스트 케이스 번호는 1부터 시작
# 문자열 맨 앞에 f를 붙여주고, 중괄호{} 안에 직접 변수 이름이나 출력하고 싶은것
import   sys
sys.stdin = open("input.txt", "r")

T = int(input())

for i in range(1, T+1): # 1부터 T까지
    A, B = map(int, input().split())
    print(f'Case #{i}: {A+B}')
```
```python
# 11022번
# 각 테스트 케이스마다 "Case #x: A + B = C" 형식으로 출력한다. x는 테스트 케이스 번호이고 1부터 시작하며, C는 A+B이다.
import   sys
sys.stdin = open("input.txt", "r")

T = int(input())
for i in range(1, T+1): # 1부터 T까지
    A, B = map(int, input().split())
    print(f'Case #{i}: {A} + {B} = {A+B}')
```


```python
# 2577번 - 숫자의 개수
# 세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성
import sys
sys.stdin = open("0_숫자의개수.txt")

A = int(input()) # 150
B = int(input()) # 266
C = int(input()) # 427
result = list(str(A * B * C))
# [1, 7, 0, 3, 7, 3, 0, 0]

for i in range(10): # i = 0 ~ 9
    # i를 문자열로 바꿔서 count
    print(result.count(str(i)))
```
```python
# 2908번- 수의 크기를 비교
# 734와 893을 칠판에 적었다면, 상수는 이 수를 437과 398로 읽는다.
# 상수의 대답을 출력하는 프로그램
# 첫째 줄에 상근이가 칠판에 적은 두 수 A와 B
# 첫째 줄에 상수의 대답을 출력
import sys
sys.stdin = open("1_상수.txt")

T1, T2 = input().split()
T1 = int(T1[::-1]) # 역순
T2 = int(T2[::-1])

# 역순으로 만약 T1이 더 크다면 출력
if T1 > T2:
    print(T1)
# 그렇지 않으면 T2를 출력   
else:
    print(T2)
```
```python
# 8958번 - OX퀴즈
# OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점
# 첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 길이가 0보다 크고 80보다 작은 문자열이 주어진다.
import sys
sys.stdin = open("3_OX퀴즈.txt")

T = int(input()) # 정수형으로 바꿈

for i in range(T):
    a = list(input())
    cnt = 0
    sum = 0
    for i in a:
        if i == 'O': # 알파벳 O를 만나면 1식 추가
            cnt += 1
            sum = sum + cnt
        else: # 그렇지 않으면 0 
            cnt = 0
    print(sum)
```


```python
# 2609번 - 최대공약수와 최소공배수
import sys
sys.stdin = open("27_최대공약수와최소공배수.txt")
# 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력
# input 첫째 줄에는 두개의 자연수
# output 첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력
T1, T2 = map(int(input().split()))
# 구글링해서 풀었지만 오류가 발생
for i in range(min(T1, T2), 0, -1):
    if T1 % i == 0   and   T2 % i == 0:
        print(i)
        break
for i in range(max(T1, T2), (T1 * T2) + 1):
    if i % T1 == 0 and i % T2 == 0:
        print(i)
        break
---
# 유클리드 호제법
a, b = map(int, input().split())
    
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
        return a
    
def lcm(a, b):
    return a * b // gcd(a, b)
    
print(gcd(a, b))
print(lcm(a, b))

---

# math 모듈 속에 파이썬 최대공약수와 최소공배수를 구하는 함수가 내장
import math
    
a, b = map(int, input().split())
    
print(math.gcd(a, b)) # 최대공약수
print(math.lcm(a, b)) # 최소공배수
```
```python
# 2231번 - 분해합
# 자연수 N의 분해합은 N과 N을 이루는 각 자리수의 합
# M의 분해합이 N인 경우, M을 N의 생성자
# 245의 분해합은 256(=245+2+4+5)이 된다.
# 자연수 N이 주어졌을 때, N의 가장 작은 생성자를 구해내는 프로그램을 작성
import sys
sys.stdin = open("28_분해합.txt")

N = int(input()) # 입력값
result = 0 # 입력값과 비교하기 위한 변수
for i in range(1, N + 1):
    # str함수를 통해 i의 각 자리수를 A 리스트에 넣기
    A = list(map(int, str(i)))
    # 그대로인 값 i와 리스트의 합 더하기
    result = i + sum(A)
    # 합을 더한것과 비교
    if result == N:
        print(i)
        break
    # 생성자가 없다면 0 출력    
    if i == N:
        print(0)
---

n = int(input())
num_list = []
for i in range(n):
    sum_i = 0
    for j in str(i):
        sum_i += int(j)   
    if i + sum_i == n:
        num_list.append(i)
        
if num_list == []:
    print(0)
else:
    print(min(num_list))    
```
```python
# 2846번 - 오르막길
# 자전거 길은 오르막길, 내리막길, 평지
# 개강 첫 날 자전거를 타고 가면서 일정 거리마다 높이를 측정했다. 상근이는 가장 큰 오르막길의 크기를 구하려고 한다.
# 측정한 높이는 길이가 N인 수열
# 오르막길은 적어도 2개의 수로 이루어진 높이가 증가하는 부분 수열
# 오르막길의 크기는 부분 수열의 첫 번째 숫자와 마지막 숫자의 차이
# 12 *3 5 7 10* 6 *1 11* -->. 이 길에는 2 개의 오르막길이 있다. 밑 줄로 표시된 부분 수열이 오르막길이다. 첫 번째 오르막길의 크기는 7이고, 두 번째 오르막길의 크기는 10이다. 높이가 12와 6인 곳은 오르막길에 속하지 않는다.
import sys
sys.stdin = open("29_오르막길.txt")

N = int(input())
arr = list(map(int,(input().split())))
    
temp = arr[0] ; sum = 0
answer = []
    
for i in range(1,N):
    if arr[i] - temp >0 : #더 높은 숫자가 등장시에, 그 차이를 sum에 더하기. 
        sum += arr[i]-temp
        temp = arr[i] # 현재 수(temp) 업데이트            
    elif arr[i] == temp or arr[i]-temp<0 : #같은수 또는 더 낮은 수가 등장시에
        answer.append(sum) #오르막길이 끝났으므로 방금까지의 오르막높이 sum을 list(answer)에 추가
        temp = arr[i] # 현재 수(temp) 업데이트
        sum = 0 #sum 초기화           
answer.append(sum) # 맨 마지막에 오르막길이 등장하면 위 for문으로는 append가 안되서 추가.
if len(answer) == 0 : print(0) # 오르막이 한번도 없었다면 0 출력
else : print(max(answer))

---

n = int(input())
arr = list(map(int,input().split()))
start,end = arr[0], arr[0]
answer = 0
for i in range(1, n):
    if end >= arr[i]:
        start = arr[i]
        end = arr[i]
    else:
        end = arr[i]
    answer = max(answer,end-start)
print(answer)
```
```python
# 2953번 - 나는 요리사다
# 점수는 1점부터 5점
# 각 참가자가 얻은 점수는 다른 사람이 평가해 준 점수의 합
# 평가 점수가 주어졌을 때, 우승자와 그의 점수를 구하는 프로그램
# 첫째 줄에 우승자의 번호와 그가 얻은 점수를 출력
import sys
sys.stdin = open("30_나는요리사다.txt")
# 점수를 담을 리스트 score 선언
score = []
# for문을 이용하여 5번 돌면서 참가자의 점수 각각 더해 score에 추가
for i in range(5):
    score.append(sum(map(int, input().split())))
# 우승자의 번호 + 우승자의 점수
print(score.index(max(score)) + 1, max(score))
```


```python
# 1157번
words = input().upper() unique_words = list(set(words))
# 입력받은 문자열에서 중복값을 제거
cnt_list = [ ]
for x in unique_words:
    cnt = words.count(x)
    cnt_list.append(cnt)
# count 숫자를 리스트에 append
if cnt_list.count(max(cnt_list)) > 1 :
# count 숫자 최대값이 중복되면
    print('?')
else :
    max_index = cnt_list.index(max(cnt_list))
# count 숫자 최대값 인덱스(위치)
    print(unique_words[max_index])
```
```python
# 2941번
# dž는 무조건 하나의 알파벳으로 쓰이고
# d와 ž가 분리된 것으로 보지 않는다. 알파벳 소문자와 '-', '='로만 이루어져 있다.
# 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력
import sys
sys.stdin = open("33_크로아티아_알파벳.txt")

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# 한 글자로 변환을 하고 이후에 변환된 문자열의 총 글자 수

word = input()

for i in croatia :       # 문자를 변환하는 함수 replace함수를 사용
    word = word.replace(i, '*') # input 변수와 동일한 이름의 변수
print(len(word))
```
```python
# 2851번
import sys
sys.stdin = open("34_슈퍼마리오.txt")

m = []
score = 0
for i in   range(10):
    m.append(int(input()))
for j in m:
    score += j
  if score >= 100:    # 차례대로 더해가면서 100이 넘어가는 시점에서 if문을 작성
  if score - 100 > 100 - (score - j):  # 숫자를 비교해 100과 더 가까운 숫자
            score -= j
  break
print(score)
```
```python
# 7568번
# 키와 몸무게, 이 두 개의 값으로 표현하여 그 등수를 매겨 표현
# 더 큰 덩치의 사람이 k명이라면 그 사람의 덩치 등수는 k+1
# 덩치 등수를 구해서 그 순서대로 첫 줄에 출력
#  각 덩치 등수는 공백문자로 분리
import sys
sys.stdin = open("35_덩치.txt")

num_student = int(input())
student_list = []
  
for _ in range(num_student):
    weight, height = map(int, input().split())
    student_list.append((weight, height))
 
for i in student_list:
    rank = 1
for j in student_list:
    if i\[0\] < j\[0\] and i\[1\] < j\[1\]:
        rank += 1
    print(rank, end = " ")
```


```python
# 23825번 - SASA 모형을 만들어보자
# 당신은 SASA 연못에서 알파벳 S 모양의 블록 N개와 알파벳 A 모양의 블록 M개를 건졌다. 태영이는 연못에서 건진 블록을 이용해 학교에 전시할 SASA 모형을 최대한 많이 만들려고 한다.
# SASA 모형 1개를 만들기 위해서는, 알파벳 S 모양의 블록 2개와 알파벳 A 모양의 블록 2개가 필요하다. 태영이가 만들 수 있는 SASA 모형 개수의 최댓값
import sys
sys.stdin = open("43_SASA 모형을 만들어보자.txt")

A1, A2 = map(int(input().split()) 
print(min(A1//2, A2//2))
# map으로 나온 결과물에 바로 //2(나눗셈 후 몫을 반환) 연산 후 min에 넣음
---
# iterable 객체도 바로 min()연산 인자로 넣을 수 있다는 것을 알게 되었다.
print(min(map(int, input().split()))//2)        
```
```python
# 3052번 - 나머지
# 두 자연수 A와 B가 있을 때, A%B는 A를 B로 나눈 나머지 이다. 예를 들어, 7, 14, 27, 38을 3으로 나눈 나머지는 1, 2, 0, 2. 
# 수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다.
# 그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성
# 첫째 줄부터 열번째 줄 까지 숫자가 한 줄에 하나씩 주어진다
# 첫째 줄에, 42로 나누었을 때, 서로 다른 나머지가 몇 개 있는지 출력
import sys
sys.stdin = open("44_나머지.txt")
n = []                #list설정, 리스트나 튜플은 순서가 있음
for i in range(10):   # 0~9 반복
    a = int(input())  # 변수를 정수로
    b = a % 42        # 입력받은 변수에 42를 더한 나머지 값
    n.append(b)       # n = [39,40,41,0,1,2,40,41,0,1]
s = set(n)            # set로 중복 제거, 순서가 없음
print(len(s))         # 리스트 s의 길이 출력
```
```python
# 5622번 - 다이얼
# 숫자를 하나 누르면 다이얼이 처음 위치로 돌아가고, 다음 숫자를 누르려면 다이얼을 처음 위치에서 다시 돌려야 한다.
# 1을 걸려면 총 2초가, 한 칸 옆에 있는 숫자를 걸기 위해 1초씩 더
# 할머니는 전화 번호를 각 숫자에 해당하는 문자로 외운다
# 전화를 걸기 위해서 필요한 최소 시간을 구하는 프로그램을 작성
import sys
sys.stdin = open("45_다이얼.txt")

alpabet = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
word = input()
time = 0
for i in range(len(word)):
    for j in alpabet:
        if word[i] in j:
            time += alpabet.index(j) + 3 # 3초씩 더함
print(time)            
```
```python
# 1292번 - 쉽게 푸는 문제
# 1을 한 번, 2를 두 번, 3을 세 번, 이런 식으로 1 2 2 3 3 3 4 4 4 4 5 .. 이러한 수열을 만들고 어느 일정한 구간을 주면 그 구간의 합을 구하는 것이다.
# 첫째 줄에 구간의 시작과 끝을 나타내는 정수
# 첫번째 숫자부터 끝번째 숫자까지 합 출력
import sys
sys.stdin = open("46_쉽게푸는문제.txt")

n1, n2 = map(int,input().split())
arr = [0]
             
for i in range(46):
    for j in range(i):
        arr.append(i)
 
print(sum(arr[n1:n2+1]))   # 구간 합을 구할 때 누적 합을 구하지 않고도 sum + slicing 함수로 구할 수 있다
```
```python
# 1357번 - 뒤집힌덧셈
# 어떤 수 X가 주어졌을 때, X의 모든 자리수가 역순이 된 수를 얻을 수 있다. Rev(X)를 X의 모든 자리수를 역순으로 만드는 함수라고 하자. 예를 들어, X=123일 때, Rev(X) = 321이다. 그리고, X=100일 때, Rev(X) = 1이다
# 두 양의 정수 X와 Y가 주어졌을 때, Rev(Rev(X) + Rev(Y))를 구하는 프로그램을 작성
import sys
sys.stdin = open("47_뒤집힌덧셈.txt")

x, y = map(str,input().split())    # 문자열로 입력을 받아 뒤집어준다.
s = str(int(x[::-1]) + int(y[::-1])) # int형으로 변환하여 더해준다음 다시 str형으로 바꿔준다
print(int(s[::-1]))  # 뒤집어준다음 다시 정수형으로 바꿔준다

---

x, y = map(str,input().split())

rev_x = int(a[::-1])  # 321
rev_y = int(b[::-1])  # 001 == 1
rev_xy =str(rev_x + rev_y)[::-1] # 321 + 1 = 322 == 223
print(int(rev_xy))
```
```python
# 10773번 - 제로
#  0을 외쳐서, 가장 최근에 재민이가 쓴 수를 지우게 시킨다
# 모든 수를 받아 적은 후 그 수의 합 출력
# import sys
# sys.stdin = open("제로.txt")
# Tast_case = map(int, input())
'''
4 -> 입력 개수
3
0
4
0
'''
K = int(input())
input_list = []
for _ in range(K):
    input_list.append(int(input()))
# input1 = [3, 0, 4, 0]
# input2 = [1, 3, 5, 4, 0, 0, 7, 0, ,0, 6]

for elem in input2:
    if elem != 0:
        stack.append(elem)
    else:
        stack.pop()
print(sum(stack)) 
```
```python
# 2161번 - 카드1
# 제일 위에 있는 카드를 바닥
# 제일 위에 있는 카드를 제일 아래에 있는 카드 밑
# 버린 카드들을 순서대로 출력하고, 마지막에 남게 되는 카드를 출력하는 프로그램을 작성
---
# 큐를 이용한 풀이
n = int(input())
queue = list(range(1, n+1))
while len(queue) > 1:
    print(queue.pop(0), end = " ")
    queue.append(queue.pop())
print(queue[0])    
---
# 덱을 이용한 풀이
n = int(input())
queue = deque(range(1, n+1))
while len(queue) > 1:
    print(queue.popleft(), end = " ")
    queue.append(queue.popleft())
print(queue[0])
# 덱을 이용하면 속도가 빠름, 대부분 댁을 이용
```

```python
# 2161번 - 카드1
import sys
sys.stdin = open('53_카드1.txt')
from collections import deque
n = int(input())
queue = deque(range(1, n+1))
while len(queue) > 1:
    print(queue.popleft(), end = " ")
    queue.append(queue.popleft())
print(queue[0])
```
```python
# 23253번 - 자료구조는_정말_최고야
# 나머지 과목의 교과서 N권을 방 구석에 M개의 더미로 아무렇게나 쌓아둠
# 팽개쳤던 나머지 과목의 교과서를 정리하고 번호순으로 나열
# 1부터 N까지의 번호
# 각 더미의 맨 위에 있는 교과서만 꺼낼 수 있으며, 반드시 교과서를 꺼낸 순서대로 나열
# 번호순으로 나열하기 위해서는 1번, 2번, … N−1번, N번 교과서 순으로 꺼내야 한다.
# 번호순으로 나열할 수 있는지 여부를 알려주는 프로그램을 작성해 주자.
# 첫째 줄 교과서의 수 N, 교과서 더미의 수 M
# 둘째 줄부터 2×M줄에 걸쳐 각 더미의 정보
# i번째 더미를 나타내는 첫 번째 줄에는 더미에 쌓인 교과서의 수 ki가 주어지며, 두 번째 줄에는 ki개의 정수가 공백으로 주어짐
# 각 정수는 교과서의 번호이며, 아래에 있는 교과서의 번호부터 주어진다.
# 교과서의 번호는 1$1$부터 N$N$까지의 정수가 한 번씩만 등장
import sys
sys.stdin = open('54_자료구조는_정말_최고야.txt')

n, m = map(int, input().split())
chk = True
for _ in range(m):
    n = int(input())
    lst = list(map(int, input().split()))
    if chk:
        while len(lst) > 0:
            tmp = lst.pop()
        if lst:
            if tmp > lst[-1]:
                chk = False
                break
    else:
        break
if chk:
    print("Yes")
else:
    print("No")
---
stack = [ 11, 10, 8, 5]
comparion = stack.pop()
while len(stack) ~= 0:
    if top > comparion:
        comparion = stack.pop()
    else:
        answer = "No"
        break
```
```python
# 9012번 - 괄호
# 두 개의 괄호 기호인 ‘(’ 와 ‘)’ 만으로 구성되어 있는 문자열
# 한 쌍의 괄호 기호로 된 “( )” 문자열은 기본 VPS
# x가 VPS 라면 이것을 하나의 괄호에 넣은 새로운 문자열 “(x)”도 VPS
# 두 VPS x 와 y를 접합(concatenation)시킨 새로운 문자열 xy도 VPS
#  “(())()”와 “((()))” 는 VPS 이지만 “(()(”, “(())()))” , 그리고 “(()” 는 모두 VPS 가 아닌 문자열
# VPS 인지 아닌지를 판단해서 그 결과를 YES 와 NO
T = int(input())
for i in range(T):
    stack = input()
    stack_list = list(stack)
    sum = 0
    for i in stack_list:
        if i == '(':
            sum += 1
        elif i == ')':
            sum -= 1
        if sum < 0:
            print('No')
            break
    if sum > 0:
        print('No')
    elif sum == 0:
        print('No')
---
T = int(input())
for i in range(T):
    stack = []
    stack_list = input()
    for i in stack_list:
        if i == ')':
            stack.append(i)
        elif i == '(':
            if stack:
                stack.pop()
            else:
                print('No')
                break
   else:            
        if not stack:
            print('Yes')
        else:
            print('No')
---
import sys #많은 양의 괄호를 불러오기 때문에
t =int(input()) #test case
for i in range(t):
    stack = []
    paren = sys.stdin.readline().strip() #리스트 값으로 받았는데 구글링 해보니 그냥 input을 받음

    for j in paren:
        if j == '(':
            stack.append(j) #( 가 있으면 추가
        elif j == ')': #) 가 있으면 제거 => ()VPS 가 완성되면 되기 때문 
            if stack :
                stack.pop()
            else :
            print('NO') # 둘 다 아니라면 문자열이므로 NO 출력
            break #break도 안 쓰고 냅다 if랑 else만 써서 답이 안 나옴
    else: #내가 틀린 부분 -> 여기서 else 안에 if문을 넣어야함 #break가 끊기지 않았을 때 
        if not stack:
            print('YES') #break로 끊기지 않고 스택이 비어있으면 VPS맞음 
        else :
            print('NO') #break가 안 걸려도 스택에 괄호가 있으면 문자열이므로 NO
```

```python
# 10546번 - 배부른 마라토너
import   sys

sys.stdin = open('60_배부른마라토너.txt')

n = int(input())
# person : 참가한 사람들의 dict
# finish : 완주한 사람들의 dict
person = dict()
finish = dict()
answer = ""
for i in range(n):
    name = input().rstrip()
    if name in person:
        person[name] += 1
    else:
        person[name] = 1
for i in range(n-1):
    name = input().rstrip()
    if name in finish:
        finish[name] += 1
    else:
        finish[name] = 1
for n in person.keys():
#  참가자에는 있지만 완주자에는 없다면 해당 키가 정답
    if n not in finish :
        answer = n
        break
    else:
#  참가자의 value와 완주자의 value가 다르다면 해당 키가 정답
        if person[n] != finish[n]:
            answer = n
            break
print(answer)
```
```python
input = sys.stdin.readline
```
```python
# 1269번 - 대칭 차집합
import   sys
sys.stdin = open('61_대칭차집합.txt')
 
# 대칭 차집합의 원소의 개수를 출력
# 두 집합 A와 B가 있을 때, (A-B)와 (B-A)의 합집합을 A와 B의 대칭 차집합
# set 자료형을 정말 유용하게 사용하는 경우는 교집합, 합집합, 차집합을 구할 때
# set는 순서가 없고, 고유한 값, 값이 변하는 객체(mutable)
a, b = map(int, input().split())
a = set(map(int, input().split())) # set를 이용해 교집합을 구한다.
b = set(map(int, input().split())) # set를 이용해 교집합을 구한다.

print(len(a-b) + len(b-a)) # a, b에 대해 a-b와 b-a의 길이를 더 해주면 된다.
# print(len(a^b))                  # 대칭 차집합 구하기
```
```python
# 11286번 - 절댓값 힙
import sys
sys.stdin = open('62_절댓값힙.txt')
import heapq  # 최소 힙(min heap) 자료구조
from sys import stdin

n = int(stdin.readline())
heap=[] # heapq 모듈을 이용함으로써 리스트를 최소 힙처럼 다룸
for _ in range(n):
    x = int(stdin.readline())
    if x == 0:
        if heap:
            print(heapq.heappop(heap)[1]) # heappop(), 대상리스트를 넘기면 가장 작은 원소를 삭제하고 값을 리턴
        else:
            print(0)
        else:
            heapq.heappush(heap, (abs(x),x))  \# heappush(), 첫번째 인자는 원소를 추가할 대상 리스트, 두번째 인자는 추가할 원소
```
```python
# 2750번 - 수 정렬하기
import   sys
sys.stdin = open('64_수정렬하기.txt') 

n = int(input())
list = [] # 숫자들을 담기 위한 리스트
for i in range(n):            # 리스트에 n개의 숫자들을
    list.append(int(input())) # input 추가하여
list.sort() # 오름차순 정렬
for i in list:          # 리스트에 정렬된 n개의 숫자들을
    print(i)         # 출력하기
```
```python
# 4949번 - 균형잡힌 세상
while True:
    str = input()
    if str == '.': # 종료 조건을 만나면
        break      # break해준다
    stack = []     # stack 리스트에 발생 시작되는 괄호 저장
    temp = True    # temp = 임시저장공간 변수
    for i in str:    # 문자열 str에서 괄호 검사
        if i == '(' or i == '[': # ( 또는 \[
            stack.append(i)# stack 리스트에 발생 시작되는 괄호 저장
        elif i == ')': # elif를 이용해 ) 검사
            if not stack or stack[-1] == '[': # 검사를 해주어 대괄호가 오면 스택을 비워나감
                temp = False  # 스택이 비워져있거나 마지막이 짝이 안맞는다면 temp를 False로 바꿔주고
                break  # break 해준다
            elif stack[-1] == '(': # 검사하여 소괄호가 나오면 스택을 비움
                stack.pop()   # pop를 이용해 요소 삭제
        elif   i == ']': #
            if not stack or stack[-1] == '(': #
                temp = False   #
                break  #
            elif   stack[-1] == '[': #
                stack.pop()                      #
    if temp == True and not stack: # temp가 True이거나 stack 리스트가 비어있으면
        print('yes') # Yes 출력
    else:            # 그렇지 않으면
        print('no')  # No 출력
```
```python
def solution(s):
    word = s
    dic_ = { '0' : 'zero', '1' : 'one', '2' : 'two', '3' : 'three', '4' : 'four', '5' : 'five', '6' : 'six', '7' : 'seven', '8' : 'eight', '9' : 'nine' }
    for key, value in dic_.items(): #여기서부터 구글링 key값만 어떻게 출력하는지 모르겠어서,, #items는 key와 value를 튜플로 묶은 값
        word = word.replace(value, key)
        return int(word)
```
```python
# 1236번 - 성지키기
import sys
sys.stdin = open('69_성지키기.txt')
from pprint import pprint
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for i in range(n)]
pprint(matrix)
---
n,m = map(int,input().split())
castle=[]
for _ in range(n):
    castle.append(input())   
row = []
col = []
for i in range(n):
    row.append("X" not in castle[i])        
for j in range(m):
    col.append("X" not in [castle[i][j] for i in range(n)])            
print(max(sum(row),sum(col)))
```
```python
# 5533번 - 유니크
# 1이상 100 이하의 정수
# 각 플레이어는 자신과 같은 수를 쓴 사람이 없다면, 자신이 쓴 수와 같은 점수를 얻는다. 만약, 같은 수를 쓴 다른 사람이 있는 경우에는 점수를 얻을 수 없다.
# 게임을 3번 했다.
# 3번 게임에서 얻은 총 점수를 구하는 프로그램을 작성
import sys
sys.stdin = open('70_유니크.txt')

n = int(input())

first = []
second = []
third = []
for i in range(n):
    a, b, c = map(int, input().split())
first.append(a)
second.append(b)
third.append(c)
for j in range(n):
    score = 0
    if first.count(first[j]) == 1:
        score += first[j]
    if second.count(second[j]) == 1:
        score += second[j]
    if third.count(third[j]) == 1:
        score += third[j]
print(score)
```
```python
# 2167번 - 2차원 배열의 합
# (i, j) 위치부터 (x, y) 위치까지에 저장되어 있는 수들의 합
# i행 j열
# 배열의 크기 N, M
# K개의 줄에는 네 개의 정수로 i, j, x, y
# K개의 줄에 순서대로 배열의 합을 출력
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
memo = [[0] * (m+1) for _ in range(n+1)]
 
for i in range(1, n+1):
    for j in range(1, m+1):
        memo[i][j] = arr[i-1][j-1] + memo[i][j-1] + memo[i-1][j] - memo[i-1][j-1]
 
k = int(input())
for _ in range(k):
    i, j, x, y = map(int, input().split())
    print(memo[x][y] - memo[i-1][y] - memo[x][j-1] + memo[i-1][j-1])
```
```python
# 1100번 - 하얀 칸
# 체스판은 8×8크기
# 가장 왼쪽 위칸 (0,0)은 하얀색
# 하얀 칸 위에 말이 몇 개 있는지 출력하는 프로그램을 작성
# 첫째 줄부터 8개의 줄에 체스판의 상태가 주어진다. ‘.’은 빈 칸이고, ‘F’는 위에 말이 있는 칸
chess = []
for _ in range(8):
    chess.append(list(map(str, list(input()))))
answer = 0
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:       #하얀칸일 경우
            if chess[i][j] == 'F': #F있을 경우
                answer += 1
print(answer)
---
import sys
input = sys.stdin.readline
```
```python
# 5와 6의 차이
a, b = input().split() #a와 b를 input 받음(map사용 X => 정수일 필요가 없음) str로 map 써도 됨 #replace는 문자열만 가능
min = int(a.replace('6', '5')) + int(b.replace('6', '5')) #6은 5로 바꾸고(5가 더 작기 때문에 최솟값)
max = int(a.replace('5', '6')) + int(b.replace('5', '6')) #5는 6으로 바꿈
print(min, max)
```
```python

```
```python

```
```python

```
```python

```
