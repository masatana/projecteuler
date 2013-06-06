# -*- coding: utf-8 -*-

def gen_prime():
    D = {}
    q = 2

    while True:
        if q not in D:
            yield q
            D[q*q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p+q,[]).append(p)
            del D[q]
        q += 1

for i, p in enumerate(gen_prime()):
    if i >= 10001:
        break
    print p

