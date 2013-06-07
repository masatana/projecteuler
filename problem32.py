# -*- coding: utf-8 -*-

def check(i, j, k):
    li = [int(x) for x in list(str(i))]
    lj = [int(x) for x in list(str(j))]
    lk = [int(x) for x in list(str(k))]
    l = li + lj + lk
    if 0 in l:
        return False
    elif len(set(l)) == 9:
        return True
    else:
        return False

ans = 0
for i in range(1, 10000):
    for j in range(1, 10000):
        k = i * j 
        if check(i, j, k):
            ans += k
print ans


