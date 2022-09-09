import sys

print("--⎝-༼¸◕ˇ‸ˇ◕˛ ༽-⎠--")
print("input을 입력하시오. (´ཀ`)a")

N, X = map(int, input().split())
A = list(map(int, input().split()))
for i in A:
    if i < X:
        print(i, end=" ")


print("⎛⎝(•‿•)⎠⎞")