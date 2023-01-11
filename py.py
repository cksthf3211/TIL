import sys
input = sys.stdin.readline
from collections import deque

n = input()
n_list_1 = list(map(int, input().split()))
# print(n_list) [2, 4, -10, 4, -9]

n_list_2 = sorted(list(set(n_list_1)))
# print(n_list) [-10, -9, 2, 4]

dic = {n_list_2[i] : i for i in range(len(n_list_2))}
# print(dic) {-10: 0, -9: 1, 2: 2, 4: 3}

for i in n_list_1:
    print(dic[i], end=' ') # 2 3 0 3 1