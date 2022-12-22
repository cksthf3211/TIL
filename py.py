import sys
input = sys.stdin.readline
 
n = int(input())  # 색종이 수
paper = [[0 for i in range(101)] for i in range(101)] # 2차원 배열 생성

for i in range(n):
    x,y = map(int, input().split()) # input 받아옴
    for j in range(x, x+10):        # x~ x+10까지 지정
        for k in range(y, y+10):    # y~ y+10까지 지정
            paper[j][k] = 1         # 다 1로 바꿔버림
            
cnt = 0

for row in paper:
    cnt += row.count(1)             # 2차원 배열인 paper 안에서 1로 바꾼 부분을 출력

print(cnt)