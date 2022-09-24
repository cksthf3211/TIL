import sys
input = sys.stdin.readline

n = int(input())
cnt = 0

for i in range(n):
    num = list(map(int, input()))
    avg = sum(num) / n
    center = num.sort() # 중앙값 미완
    bin = set(num) # 최빈값 미완
    rang = len(max(num) - min(num))

