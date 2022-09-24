import sys
input = sys.stdin.readline

n = int(input())
n_list = []

for i in range(n):
    x, y = map(int, input().split())
    n_list.append((x, y))

n_list.sort(key = lambda x:(x[1], x[0]))

for j in n_list:

    print(*j)