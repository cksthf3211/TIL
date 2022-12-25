import sys
input = sys.stdin.readline
from collections import deque

# n = int(input())
# n_list = []
# num = deque()

# for i in range(n):
    
#     while num:
        
#         print(-1)
#         break
for i in range(5):
    for j in range(i+1):
        print('*', end='')
    print('')