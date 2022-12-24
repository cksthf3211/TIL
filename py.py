import sys
input = sys.stdin.readline
from collections import deque
 
n, m = map(int, input(). split())
n_list = list(map(int, input().split()))
num = deque()

print(n_list)    # [1, 2, 3]

for i in range(n):
    num.append(i+1)
    
print(num)       # deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

cnt = 0          # 2, 3번 수행하면 카운트 올리기

for i in n_list:
    while num:   # 뽑을 때까지 계속 
        if num[0] == i:  # dq의 첫인덱스가 뽑아내려는 수의 위치와 같다면 1번 수행
            num.popleft()
            break    # deque([4, 5, 6, 7, 8, 9, 10])
        
        else:
            if num.index(i) < len(num) / 2:    # 뽑아내려는 수의 위치 인덱스가 num의 길이를 반으로 나눈것보다 작을때는 왼쪽으로 움직여야 최소
                while num[0] != i:             # num의 첫번째 인덱스가 i와 같아질때까지 반복
                    num.append(num.popleft())
                    cnt += 1
            
            else:
                while num[0] != i:
                    num.appendleft(num.pop())
                    cnt += 1
                    
print(cnt)