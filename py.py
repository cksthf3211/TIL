import sys
input = sys.stdin.readline
from collections import deque
import heapq
sys.setrecursionlimit(10 ** 6)         #  재귀 깊이 늘려줌줌이

n, m, r = map(int, input().split())    # 정점 수, 간선 수, 시작 정점
graph = [[] for _ in range(n+1)]       # 연결노드 그래프 초기화 (1번노드와 인덱스 값이 같게 하기 위해서 n+1로 )
cnt = 1                                # 방문 순서
visited = [0] * (n+1)                  # 방문 순서 그래프

# print(graph) [[], [], [], [], []]
# print(visited) [0, 0, 0, 0, 0, 0]

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)                 # u가 시작 정점, 연결 되있음 v랑
    graph[v].append(u)                 # v가 끝나는 정점, 연결 되있음 u랑
# graph.sort()
# print(graph) [[], [4, 2], [1, 3, 4], [2, 4], [1, 2, 3], []]

for i in graph:
    i.sort(reverse=True)                           # 오름차순으로 정렬
# print(graph) [[], [2, 4], [1, 3, 4], [2, 4], [1, 2, 3], []]
print(graph)
def dfs(graph, r, visited):            # v: 정점 집합, e: 간선 집합, r: 시작 정점
    global cnt
    visited[r] = cnt
    for i in graph[r]:
        if visited[i] == 0:
            cnt += 1
            dfs(graph, i, visited)

dfs(graph, r, visited)
# print(visited) [0, 1, 2, 3, 4, 0]
# print(cnt) 4 

for i in range(1, n+1):
    print(visited[i])