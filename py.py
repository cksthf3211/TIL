import sys
# sys.stdin = open('py.txt')
input = sys.stdin.readline
from collections import deque
from pprint import pprint

n, m = map(int, input().split())           # 지도의 크기
graph = [list(map(int, input().rstrip())) for i in range(n)]

#visited = [ [0] * m for i in range(n)]

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
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        if x == n - 1 and y  == m - 1:
            print(graph[x][y])
        
        # 4가지 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1
            
            # if nx < 0 or ny < 0 or nx >= n or ny >= m: # 가장자리 벽
            #     continue
            
            # if graph[nx][ny] == 0:  # 0은 이동할 수 없음
            #     continue
            
            # if graph[nx][ny] == 1:
            #     queue.append((nx, ny))
            #     graph[nx][ny] == graph[x][y] + 1
                
    return graph[n-1][m-1]

print(bfs(0,0)) 

