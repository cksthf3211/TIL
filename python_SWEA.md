# SW Expert Academy
```python
# 예제
for test_case in range(1, T + 1):
    a = map(int, input().split())
    print(list(a))
```

```python
# 문제번호 1933 - 간단한 N 의 약수
import sys

sys.stdin = open("input.txt", "r")
N = int(input())

for i in range(N):
    if N % (i+1) == 0:
        print(i+1, end=' ')
```
```python
# 문제번호 2019 - 더블더블
# 1부터 시작하여 2씩 곱해나가자
# input 8
# 내가 한거
T = int(input())
for i in range(1, T*2):
    print(i)
#
T = int(input())
for i in range(T+1):
    print((2**i), end = ' ')
```
```python
# 문제번호 2050 - 알파벳을 숫자로 변환
# input ABCDEFGHIJKLMNOPQRSTUVWXYZ
# 아스키코드 a = 65
T = input()
for i in T:
    print(ord(i)-64, end = ' ')
```
```python
# 문제번호 2029 - 몫과 나머지 출력하기
import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for i in range(1, T+1):
    a, b = map(int, input().split())
    print("#{} {} {}".format(i, a//b, a%b))
```
```python
# 문제번호 1284 - 수도요금 경쟁
import sys
sys.stdin = open("input.txt", "r")
# A사 : 1L * P원
# B사 : Q + 
# R이하 : Q
# R초과 : Q + S*(사용량-R)
T = int(input())
for i in range(1, T+1):
    P, Q, R, S, W = map(int, input().split())
    #print(P, Q, R, S, W)
    A = W * P
    if R > W:
                B = Q
        else:
             B = Q + S*(W-R)
                print(f'#{test_case} {min(A, B)}')
```
```python
# 
```
