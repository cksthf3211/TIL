# SW Expert Academy
> [SW Expert Academy](https://swexpertacademy.com/main/code/problem/problemList.do)
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
# 1204번 - 최빈수 구하기 1일차
import sys

sys.stdin = open("_최빈수구하기.txt")
# 1000명의 수학 성적
# 최빈수를 이용하여 학생들의 평균 수준을 짐작
# 최빈수는 특정 자료에서 가장 여러 번 나타나는 값
# 최빈수를 출력하는 프로그램을 작성
# 학생의 수는 1000명이며, 각 학생의 점수는 0점 이상 100점 이하의 값
# 첫 번째 줄에 테스트 케이스의 수 T
#  테스트 케이스의 첫 줄에는 테스트 케이스의 번호가 주어지고 그 다음 줄부터는 점수
# #부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스에 대한 답을 출력
T = map(int,input().split())

```
```python
# 10505번 - 소득 불균형 1일차
import sys

sys.stdin = open("_소득불균형.txt")
# n명의 사람의 소득이 주어졌을 때 이 중 평균 이하의 소득을 가진 사람들의 수를 출력
# 첫 번째 줄에 테스트 케이스의 수 T
# 이후 T개의 테스트 케이스에 대해 각각 두 줄
# 첫 번째 줄에는 정수의 개수 N
# 두 번째 줄에는 각 사람의 소득을 뜻하는 N개의 양의 정수
# 각각 1 이상 100,000 이하
# 각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호 의미, 1부터 시작)를 출력하고,
# 각 테스트 케이스마다 한 줄씩 평균 이하의 소득을 가진 사람들의 수를 출력한다.

```

```python
# 11856번 - 반반

```

```python
# 2465번 - 창용 마을 무리의 개수

```
