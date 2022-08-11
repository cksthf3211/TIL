k = input().split(',')
c = {}
for i in range(k):
    if i in c:
        c[k] += 1
    else:
        c[k] = 1
print('\n------------카운팅결과출력-----------')
for key1, value1 in c.items():
    print('{0:40s}  {1:5s}  '.format(key1, str(value1)))