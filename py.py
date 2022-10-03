import sys
sys.setrecursionlimit(10000) # 재귀를 사용해서 풀어야 하는 문제라면, 위 코드를 상단에 쓰는 것은 선택이 아닌 필수
# 기본 재귀 깊이 제한은 1000
# input = sys.stdin.readline

# dfs 정의
def dfs(x, y):
    # 상하좌우 확인을 위해 dx, dy 생성
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]

    # 네 방향 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < m) and (0 <= ny < n):  # nx:ny ↔ M:N 범위 참고
            if graph[ny][nx] == 1:
                graph[ny][nx] = -1  # 배추가 인접할 때 체커
                dfs(nx, ny)

# 1
t = int(input()) # 테스트케이스

for i in range(t):
    m, n, k = map(int, input(). split()) # 가로:m, 세로:n, 위치의 개수:k
    graph = [[0] * m for i in range(n)]
    cnt = 0
    
    # 배추 위치에 1 표시
    for j in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1
        
# 2
    # dfs 활용하여 배추 그룹 수 세기
    for x in range(m):
        for y in range(n):
            if graph[y][x] == 1:
                dfs(x, y)
                cnt += 1
                
    print(cnt)