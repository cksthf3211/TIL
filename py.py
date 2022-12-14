import sys
input = sys.stdin.readline

n, m = map(int, input().split())

a = [] # 행렬 받을 리스트
b = [] # //

for i in range(n):
    i = list(map(int, input().split()))
    a.append(i) # [[1, 1, 1], [2, 2, 2], [0, 1, 0]] = a
    
for j in range(n):
    j = list(map(int, input().split()))
    b.append(j) # [[3, 3, 3], [4, 4, 4], [5, 5, 100]] = b
    
for i in range(n):
    for j in range(m):
        print(a[i][j] + b[i][j], end=" ")
    print("감사합니다")