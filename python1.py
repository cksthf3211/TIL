n = int(input())
n1 = 0
sum = 0
while n1 <= n:
    n1 = n1 + 1
    if n1 % 2 == 1:
        continue
    sum = sum + n1    
print(sum)