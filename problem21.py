# -*- coding: utf-8 -*-

import functions

def sum_proper_divisors(n):
    return sum([x for x in functions.gen_factors(n)]) - n

d = {x:sum_proper_divisors(x) for x in range(10000)}

l = []

for k, v in d.items():
    if v < 10000:
        if k == d[v] and k != v:
            l.append(k)
print sum(l)
