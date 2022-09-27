import sys
input = sys.stdin.readline

word = input()
s = 'abcdefghijklmnopqrstuvwxyz'

for i in s:
    if i in word:
        print(word.index(i), end=' ')
    else:
        print(-1, end=' ')
