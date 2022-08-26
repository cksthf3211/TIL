chess = []
cnt = 0

for i in range(8):
    chess.append(list(str(input())))

for j in range(8):
    for k in range(8):
        if (j+k) % 2 == 0 and  chess[j][k] == "F":
            cnt += 1
print(cnt)