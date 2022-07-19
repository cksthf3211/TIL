import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for i in range(1, T + 1):

    a = map(int, input().split())
    
    print(f"a: {a} T: {T}")