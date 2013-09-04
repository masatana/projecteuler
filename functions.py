# -*- coding: utf-8 -*-
import random

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

def is_prime(n, k = 10):
    if n & 1 == 0:
        return False

    d = (n -1) >> 1
    while d & 1 == 0:
        d >>= 1
    for i in xrange(k):
        a = random.randint(1, n - 1)
        t = d
        y = pow(a, t, n)
        while t != n - 1 and y != 1 and y != n - 1:
            y = pow(y, 2, n)
            t <<= 1
        if not y == n - 1 and t & 1 == 0:
            return False
    return True

def is_pandigital(n, h):
    if set(str(n)) == set([str(x) for x in xrange(1, h + 1)]):
        return True
    else:
        return False
