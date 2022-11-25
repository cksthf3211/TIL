import sys
input = sys.stdin.readline

x = 64
n = int(input())
cnt = 0

while n > 0:
    if x > n:
        x = x // 2
    else:
        cnt += 1
        n -= x
print(cnt)
    