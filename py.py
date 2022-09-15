from operator import index
import sys
input = sys.stdin.readline

n_list = []
cnt = 0

for i in range(1, 10):
    n = int(input())
    n_list.append(n)


print(max(n_list), n_list.index(max(n_list))+1 ,sep="\n")

# for i in n:
#     n_list.append(n)
#     print(n_list)

# print(max(a), end="")


print("⎛⎝(•‿•)⎠⎞")