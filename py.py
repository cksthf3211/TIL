from collections import deque
import sys
read = sys.stdin.readline

def bfs(v):
    q = deque()
    q.append(v)       # 정점의 번호를 q에 append
    visit_list[v] = 1 # 방문을 하게되면 1로 바꿔줌 
    while q:                  # deque를 계속 돌리면서
        v = q.popleft()       # 방문 노드를 하나씩 빼줌
        print(v, end = " ")
        for i in range(1, n + 1): # 1~정점 개수
            if visit_list[i] == 0 and graph[v][i] == 1: # 방문을 안하고, 그래프가 1이면,
                q.append(i)       # deque에 넣어줌
                visit_list[i] = 1 # 그럼 방문 했어~ 1이야~

def dfs(v):
    visit_list2[v] = 1        # 방문을 하게되면 1로 바꿔줌
    print(v, end = " ")
    for i in range(1, n + 1): # 1~정점 개수
        if visit_list2[i] == 0 and graph[v][i] == 1:
            dfs(i)

n, m, v = map(int, read().split())            # 정점의 개수, 간선의 개수, 정점의 번호

graph = [[0] * (n + 1) for _ in range(n + 1)] # 그래프
# graph = []
# for _ in range(n+1):
#     graph.append([0] * (n+1))

visit_list = [0] * (n + 1)   # bfs에서
visit_list2 = [0] * (n + 1)  # dfs에서

for _ in range(m):
    a, b = map(int, read().split())
    graph[a][b] = graph[b][a] = 1    # 양방향(둘 다 연결됨)

dfs(v)
print()
bfs(v)