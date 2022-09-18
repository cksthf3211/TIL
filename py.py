import sys
input = sys.stdin.readline

# n, k = map(int, input().split())

# for i in n:
#     if k > a
#     a = map(int, input())

#     print(a)

n, k = map(int, input().split()) 
count = 0
coin_lst = []
for i in range(n):
    coin_lst.append(int(input()))  # 동전의 가치를 리스트에 입력

for i in reversed(range(n)):
    count += k // coin_lst[i]        # 카운트 값에 k를 동전으로 나눈 몫을 더해줌
    k = k % coin_lst[i]              # k는 동전으로 나눈 나머지로 계속 반복

print(coin_lst)
print(count)





print("⎛⎝(•‿•)⎠⎞")