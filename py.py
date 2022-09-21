import sys
input = sys.stdin.readline


c = int(input())     # 테스트케이스 개수


for i in range(c):
    cnt = 0
    n = list(map(int, input().split()))
    avg = sum(n[1:]) / n[0]

    for j in range(1, len(n)):
        if n[j] > avg:
            cnt += 1

    result = cnt / n[0] * 100

    # print(f'{round(result,3)}%')
    print(f'{result:.3f}%')



print("⎛⎝(•‿•)⎠⎞")