import sys
input = sys.stdin.readline


nums = [3, 2, 1, 3]           # 주머니괴물의 번호
monster = {}                  # 주머니괴물을 담을 주머니
lenth = round(len(nums)/2)


for i in nums:                # 괴물들 번호를 순회
    if i not in monster:      # i에(key값) 괴물이 안에 없으면
        monster[i] = 1        # key에 value를 1 줘라 (넌 한마리야)
    else:                         
        monster[i] += 1       # 아니면 value + 1 (한마리 추가)
        
    answer = len(monster)
print(len(monster))
# N/2마리의 폰켓몬을 선택하는 방법 중, 
# 가장 많은 종류의 폰켓몬을 선택하는 방법을 찾아, 그때의 폰켓몬 종류 번호의 개수를 return 하도록 solution 함수를 완성해주세요.


# nums = [3, 1, 2, 3] 이라면  
# monster = {3 : 2, 1 : 1, 2 : 1}
