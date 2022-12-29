import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations  # combinations(반복 가능한 객체, 뽑을 개수)
 
## 맵크기(N), 치킨집 최대 선택가능개수(M)
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
# print(board) [[0, 0, 1, 0, 0], [0, 0, 2, 0, 1], [0, 1, 2, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 2]]


# for i in range(n):
#     print(board[i]) 
# [0, 0, 1, 0, 0]
# [0, 0, 2, 0, 1]
# [0, 1, 2, 0, 0]
# [0, 0, 1, 0, 0]
# [0, 0, 0, 0, 2]   


# 집과 치킨집에 대한 위치 정보를 저장
# 빈칸(0), 집(1), 치킨집(2)
house = []
chicken = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 1: house.append((i, j))
        elif board[i][j] == 2: chicken.append((i, j))
 
minv = float('inf')
for ch in combinations(chicken, m):
    sumv = 0
    for home in house:
        sumv += min([abs(home[0]-i[0])+abs(home[1]-i[1]) for i in ch])
        if minv <= sumv: break
    if sumv < minv: minv = sumv
 
print(minv)
