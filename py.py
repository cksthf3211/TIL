import sys
input = sys.stdin.readline

print("input을 입력하시오.⎝-༼¸◕ˇ‸ˇ◕˛ ༽-⎠")


n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())

cnt = 0
for i in range(n):
    if a[i] > b:
        a[i] -= b
        cnt += 1

        if a[i] % c == 0:
            cnt += a[i] // c
        else:
            cnt += a[i] // c + 1
    else:
        cnt += 1

print(cnt)


print("⎛⎝(•‿•)⎠⎞")