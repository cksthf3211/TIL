import sys

print("⎝༼¸◕ˇ‸ˇ◕˛ ༽⎠")
print("input을 입력하시오. (´ཀ`)a")

t = int(input())

for i in range(1, t+1):
    a, b = map(int, sys.stdin.readline().split())
    print(f"Case #{i}: {a} + {b} = {a+b}")


print("⎛⎝(•‿•)⎠⎞  ⎛⎝(•‿•)⎠⎞  ⎛⎝(•‿•)⎠⎞  ⎛⎝(•‿•)⎠⎞")