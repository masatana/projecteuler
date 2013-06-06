# -*- coding: utf-8 -*-
from decimal import Decimal
import math
from itertools import groupby

def gen_surplus(n):
    i = 1
    t = 0
    while True:
        tmp_i = i
        i = (10 ** t) * i
        if n > i:
            t += 1
            i = tmp_i
            continue
        tmp = i % n
        i %= n
        if tmp == 0:
            break
        yield tmp
max_i = 0
max_n = 0
tmp = []
for i in range(2, 1000):
    for n in gen_surplus(i):
        print i, n
        if n in tmp:
            break
        else:
            tmp.append(n)
    if max_n < len(tmp):
        max_i = i
        max_n = len(tmp)
    tmp = []
print max_i
