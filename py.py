import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print('Equilateral')
if a + b + c == 180 and a == b or a == c or b == c:
    print('Isosceles')
if a + b + c == 180 and a != b or a != c or b != c:
    print('Scalene')
else:
    print('Error')