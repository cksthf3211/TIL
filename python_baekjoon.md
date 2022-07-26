# BAEKJOON
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

```
```python

```
```python

```
```python

```
```python

```
```python

```
