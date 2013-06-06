# -*- coding: utf-8 -*-

def gen_triangle_numbers():
    i = 1
    tmp = 0
    while True:
        yield i + tmp
        tmp += i
        i += 1

def gen_factors(n):
    for i in range(1, (n / 2) + 1):
        if n % i == 0:
            yield i
    yield n

def gen_prime_numbers():
    D = {}
    q = 2
    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1

