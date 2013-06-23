# -*- coding: utf-8 -*-

def check(n):
    l = [x for x in list(n)]
    if '0' in l:
        return False
    elif set(l) == set(['1','2','3','4','5','6','7','8','9']) and len(l) == 9:
        return True
    else:
        return False

for i in range(10000, 1, -1):
    j = 0
    n = '' 
    while True:
        j += 1
        n += str(i * j)
        if len(n) >= 9:
            break
    if check(n):
        print n
        break
