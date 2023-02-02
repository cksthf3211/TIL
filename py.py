import sys
# sys.stdin = open('py.txt')
input = sys.stdin.readline
from collections import deque
from pprint import pprint

n, m = map(int, input().split())           # 지도의 크기
graph = [list(map(int, input().rstrip())) for i in range(n)]  # 행렬 만들기
n_list = []
visited = [ [0] * m for i in range(n)]
cnt = 1

# (1, 1)에서 출발 (N, M)의 위치로 이동
# 지나야 하는 최소 칸 수 출력

# print(graph)
# [[1, 0, 1, 1, 1, 1], 
# [1, 0, 1, 0, 1, 0], 
# [1, 0, 1, 0, 1, 1], 
# [1, 1, 1, 0, 1, 1]]

# print(visited)
# [[0, 0, 0, 0, 0, 0], 
# [0, 0, 0, 0, 0, 0], 
# [0, 0, 0, 0, 0, 0], 
# [0, 0, 0, 0, 0, 0]]

dx = [0, 1, -1, 0]
dy = [-1, 0, 0, 1]

def bfs(x, y):
    queue = deque()
    queue.append(x, y)
    
    while queue:
        x, y = queue.popleft()
        
        # 4가지 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]