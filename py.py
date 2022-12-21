import sys
input = sys.stdin.readline

def hansu(num) :
    hansu_cnt = 0
    for i in range(1, num+1):
        num_list = list(map(int,str(i)))
        if i < 100:
            hansu_cnt += 1  # 100보다 작으면 모두 한수
        elif num_list[0]-num_list[1] == num_list[1]-num_list[2]:
            hansu_cnt += 1  # x의 각 자리가 등차수열이면 한수
    return hansu_cnt

num = int(input())
print(hansu(num))