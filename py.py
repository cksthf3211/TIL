import sys
input = sys.stdin.readline
from collections import deque
 
n = int(input())
card = deque()

for i in range(n, 0, -1):
    card.append(i)                  # deque([6, 5, 4, 3, 2, 1])
 
while len(card) > 1:
    card.pop()                  # 1번 카드 버림 (1)
    card.appendleft(card.pop()) # 2번 카드 맨 밑으로 
    
print(card[0])
paper = [[0 for i in range(101)] for i in range(101)] # 2차원 배열 생성