# -*- coding: utf-8 -*-
import functions

def gen_abundant_numbers():
    n = 1
    while True:
        if sum([x for x in functions.gen_factors(n)]) - n >  n:
            yield n
        n += 1


l = []
for x in gen_abundant_numbers():
    if x > 28200:
        break
    l.append(x)
mat = {x: 0 for x in range(1, 28123)}
for i in l:
    for j in l:
        mat[i + j] = 1

print sum([k for k, v in mat.items() if k <= 28123 and v == 0])
