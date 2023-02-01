import sys
sys.stdin = open('py.txt')
input = sys.stdin.readline
from collections import deque
from pprint import pprint

n = int(input())           # 지도의 크기
graph = [list(map(int, input().rstrip())) for i in range(n)]  # 행렬 만들기
n_list = []
visited = [ [0] * n for i in range(n)]

# print(graph)
# [[0, 1, 1, 0, 1, 0, 0],
#  [0, 1, 1, 0, 1, 0, 1],
#  [1, 1, 1, 0, 1, 0, 1],
#  [0, 0, 0, 0, 1, 1, 1],
#  [0, 1, 0, 0, 0, 0, 0],
#  [0, 1, 1, 1, 1, 1, 0],
#  [0, 1, 1, 1, 0, 0, 0]]

# 한 점을 기준으로 (위 아래 왼쪽 오른쪽) 으로 한칸 씩 이동할 좌표
dy = [0,0,1,-1] # 위
dx = [1,-1,0,0] # 아래

def bfs(y, x):
    cnt = 1
    queue = deque()
    queue.append((y, x))
    visited[y][x] = 1
    
    while queue:
        y, x = queue.pop()
                
        if graph[y][x] == 1:
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < n and graph[ny][nx] == 1 and visited[ny][nx] == 0:
                    queue.append((ny, nx))
                    cnt += 1
                    visited[ny][nx] = 1
    return cnt

for i in range(n):
    for j in range(n):
        
        if graph[i][j] == 1 and visited[i][j] == 0:
            n_list.append(bfs(i, j))

# pprint(visited)
# [[0, 1, 1, 0, 1, 0, 0],
#  [0, 1, 1, 0, 1, 0, 1],
#  [1, 1, 1, 0, 1, 0, 1],
#  [0, 0, 0, 0, 1, 1, 1],
#  [0, 1, 0, 0, 0, 0, 0],
#  [0, 1, 1, 1, 1, 1, 0],
#  [0, 1, 1, 1, 0, 0, 0]]


# pprint(n_list)
# [7, 8, 9]

n_list.sort() # 오름차순

print(len(n_list)) # 총 단지 수

for k in n_list:   # 각 단지마다 집의 수
    print(k)