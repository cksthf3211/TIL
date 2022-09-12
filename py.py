import sys

print("--⎝-༼¸◕ˇ‸ˇ◕˛ ༽-⎠--")
print("input을 입력하시오. (´ཀ`)a")

n = int(input())          # 68
num = n
cnt = 0                   # 사이클 수

while True:               # while == 1
    a = num // 10         # 6
    b = num % 10          # 8
    c = (a + b) % 10      # 
    num = (b * 10) + c

    cnt += 1

    if (num == n):
        break

print(cnt)
    


print("⎛⎝(•‿•)⎠⎞")