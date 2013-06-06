# -*- coding: utf-8 -*-
from functions import *
from operator import *

prime_list = []

for i, x in enumerate(gen_prime_numbers()):
    if i > 500:
        break
    prime_list.append(x)

for i in gen_triangle_numbers():
    d = {}
    for j in prime_list:
        tmp = i
        if i < j:
            break
        while True:
            if tmp % j != 0:
                break
            if j in d:
                d[j] += 1
            else:
                d[j] = 1 + 1 # 後でどうせ1を足すので
            tmp /= j
    r = reduce(mul, d.values(), 1)
    print i
    if r > 500:
        print i
        break
