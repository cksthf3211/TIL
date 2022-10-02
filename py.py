import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
num.sort()
x = int(input())
cnt = 0

for i in range(n):
    num
    for j in range(n):
        num.reverse # num[::-1]

        if x == [i] + [j]:
            cnt += 1
        
print(cnt)