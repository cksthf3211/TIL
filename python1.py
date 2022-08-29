print("원래 일어나는 시간을 입력하세요. 시간, 분")
h, m = map(int, input().split())
print('친구가 일어날 시간은')
if m > 44:
    print(f"{h}시 {(m-45)}분")
elif m < 45 and h > 0:
    print(f"{h-1}시 {m+15}분")
else:
    print(f"{23}시 {m+15}분")