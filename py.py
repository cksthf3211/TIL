import sys
input = sys.stdin.readline

# n = int(input())
# cnt = 0

# for i in range(n):
#     num = list(map(int, input()))
#     avg = sum(num) / n
#     center = num.sort() # 중앙값 미완
#     bin = set(num) # 최빈값 미완
#     rang = len(max(num) - min(num))
import sys

input = sys.stdin.readline

n = int(input())
nums = sorted([int(input()) for _ in range(n)])
num = [[0] * 2 for _ in range(4001)]

mx = 0
print(round(sum(nums) / n)) #산술 평균
print(nums[n//2])# 중앙값

for i in nums:
    # 마이너스, 플러스 구분
    if i < 0:
        num[abs(i)][0] += 1
    else:
        num[i][1] += 1 # 반대로 플러스면 [1] +1
    mx = max(mx, num[abs(i)][0], num[abs(i)][1])
c = []
for i in range(4001):
    # 마이너스 부분
    if num[i][0] == mx and num[i][0]:
        c.append(-i)
    # 플러스 부분
    if num[i][1] == mx and num[i][1]:
        c.append(i)
# 정렬
c.sort()
# 한개라면 첫번째
if len(c) == 1:
    print(c[0])
# 두개이상 이라면 두번째꺼
else:
    print(c[1])
# 범위
print(nums[-1] - nums[0])
