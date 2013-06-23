# -*- coding: utf-8 -*-
import functions

def f(l):
    tmp = 0
    for i, j in enumerate(l):
        tmp += j * (10 ** (len(l) - 1 - i))
    return tmp

def gen_circular_number(n):
    new_n = [int(x) for x in list(str(n))]
    for i in range(len(str(n))):
        tmp = new_n.pop(0)
        new_n.append(tmp)
        yield f(new_n)

l = []
for prime in functions.gen_prime_numbers():
    ff = True
    if prime > 1000000:
        break
    if prime < 10:
        l.append(prime)
    else:
        ll = [int(x) for x in list(str(prime))]
        for dame in [0,2,4,5,6,8]:
            if dame in ll:
                ff = False
                break
        if ff:
            l.append(prime)

tmp = 0
b = True
for prime in l:
    for circular_number in gen_circular_number(prime):
        if circular_number not in l:
            b = False
            break
    if b:
        tmp += 1
    cnt = 0
    b = True
print tmp
