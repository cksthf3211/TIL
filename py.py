import sys
input = sys.stdin.readline

n = int(input())                               # 학교의 수
answer = 0                                     # 남은 사과를 모아두자구

for i in range(n):
    student, apple = map(int, input().split()) # n(학교 수)를 순회하면서 input을 받아오자
    answer += apple % student                  # 나누기 연산 후 몫이 아닌 나머지를 구하고, answer에 더해줌
    
print(answer)                                  # 남은 사과를 구하자
