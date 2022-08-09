apb = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(1, 26):
    s = apb[i:26] + apb[0:i]
    print('{:2d}  {}  '.format(i, s))