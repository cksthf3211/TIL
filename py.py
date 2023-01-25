import sys
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10 ** 6)         #  재귀 깊이 늘려줌줌이

n, m, r = map(int, input().split())    # 정점 수, 간선 수, 시작 정점
cnt = 1
visited = [0] * (n+1)
graph = [[] for _ in range(n+1)]
# print(visited) [0, 0, 0, 0, 0, 0]
# print(graph) [[], [], [], [], [], []]

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(b):
    global cnt
    
    q = deque([r])
    visited[r] = 1
    
    while q:
        b = q.popleft()
        graph[b].sort()
        
        for i in graph[b]:
            if visited[i] == 0:
                cnt += 1
                visited[i] = cnt
                q.append(i)
    
bfs(1)

#print(visited) [0, 1, 2, 4, 3, 0]
for i in visited[1:]:
    print(i)
    