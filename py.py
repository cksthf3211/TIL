import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = []

board = [ [0 for j in range(m)] for i in range(n) ] # board = [[0] * m for _ in range(n)]
#print(board) [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

r, c, d = map(int, input().split()) # 1 1 0

# d => 0,3,2,1 순서로 돌아야한다.
dx = [-1,0,1,0]
dy = [0,1,0,-1]

for i in range(n):
    graph.append(list(map(int,input().split())))
# print(graph) [[1, 1, 1], [1, 0, 1], [1, 1, 1]]

# 처음 시작하는 곳 방문 처리
board[r][c] = 1
cnt = 1

while 1:
    flag = 0
    # 4방향 확인
    for _ in range(4):
        # 0,3,2,1 순서 만들어주기위한 식
        nx = r + dx[(d+3)%4]
        ny = c + dy[(d+3)%4]
        # 한번 돌았으면 그 방향으로 작업시작
        d = (d+3)%4
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
            if board[nx][ny] == 0:
                board[nx][ny] = 1
                cnt += 1
                r = nx
                c = ny
                #청소 한 방향이라도 했으면 다음으로 넘어감
                flag = 1
                break
    if flag == 0: # 4방향 모두 청소가 되어 있을 때,
        if graph[r-dx[d]][c-dy[d]] == 1: #후진했는데 벽
            print(cnt)
            break
        else:
            r,c = r-dx[d],c-dy[d]