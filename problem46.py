# -*- coding: utf-8 -*-
import functions
import math

x = 4
l = []
while True:
    if x > 1000:
        break
    if x % 2 == 0:
        x += 1
        continue
    for p in functions.gen_prime_numbers():
        if p not in l:
            l.append(p)
        if p >= x:
            if x not in l:
                print('\t{0}, {1}'.format(x, p))
            break
        tmp = math.sqrt((x - p) / 2.0)
        if functions.is_integer(tmp):
            print(x, p, int(tmp))
            break
        else:
            pass
    x += 1

