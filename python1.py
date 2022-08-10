basedata = '''김영민, 69, 100, 100
박동식, 100, 98, 98
최민규, 88, 96, 90
동후민, 88, 98, 97
신형균, 99, 44, 66
김철규, 88, 69, 100'''
data = basedata.split( '\n')

for i in range(len(data)):
    data[i] = data[i].split(',')
    print(data[i])
for k in range(len(data)):
    sum = 0
    for j in range(1, 4):
        data[k][j] = int(data[k][j])
        sum += data[k][j]
    data[k].append(sum)
    av = int(sum/3)
    data[k].append(av)
    print(data[k])