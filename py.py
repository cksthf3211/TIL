import sys
input = sys.stdin.readline


n = int(input())
score = list(map(int,input().split()))


a = max(score)
b = sum(score)
c = b / n / a * 100



print(c)


# print(((180/3)/80)*100) # 40 80 60


print("⎛⎝(•‿•)⎠⎞")