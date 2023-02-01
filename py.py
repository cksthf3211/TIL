import sys
input = sys.stdin.readline
from collections import deque

n = int(input())           # 지도의 크기
cnt = 0
graph = [list(map(int, input().rstrip())) for i in range(n)]  # 행렬 만들기
# print(graph)
# [[0, 1, 1, 0, 1, 0, 0],
#  [0, 1, 1, 0, 1, 0, 1],
#  [1, 1, 1, 0, 1, 0, 1],
#  [0, 0, 0, 0, 1, 1, 1],
#  [0, 1, 0, 0, 0, 0, 0],
#  [0, 1, 1, 1, 1, 1, 0],
#  [0, 1, 1, 1, 0, 0, 0]]

# 한 점을 기준으로 (위 아래 왼쪽 오른쪽) 으로 한칸 씩 이동할 좌표
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(graph, x, y):
    global cnt
    
    if x < 0 or x >= n or y < 0 or y >= n:
        cnt += 1
    
    
