import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
n_list = input()
cnt = 0

for i in range(n):
  cnt += int(n_list[i])
  
print(cnt)