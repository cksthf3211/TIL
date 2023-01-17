import sys
input = sys.stdin.readline
from collections import deque
import heapq

n = int(input())
n_list = []
cnt = 0

 
for i in range(n):
    n_list.append(int(input()))
if n == 1:
    print(0)
else:
    dasom = n_list[0]
    not_dasom = sorted(n_list[1:], reverse=True)
    for index, num in enumerate(not_dasom):
        if dasom == num:
            print(1)
            break
        while(not_dasom[0] >= dasom):
            cnt += 1
            dasom += 1
            not_dasom[0] -= 1
            not_dasom = sorted(not_dasom, reverse=True)
        print(cnt)
        break