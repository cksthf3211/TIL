word = 'banana'
result = {}
for char in word:
    # 딕셔너리에 키가 있으면
    if char in result:
        # 키랑 값을 0으로 초기화
        result[char] = 1
    # 딕셔너리에 키가 없으면
    else:
        result[char] = result[char] + 1
print(result)        
