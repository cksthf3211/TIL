import sys
# sys.stdin = open('py.txt')
input = sys.stdin.readline
from collections import deque
from pprint import pprint

# n, m = map(int, input().split())

for i in range(int(input())):
    word = str(input())
    print(word[0] + word[-1])
