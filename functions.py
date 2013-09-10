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
        print D, q
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                print p
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1


def mark(s, x):
    for i in xrange(x + x, len(s), x):
        s[i] = False

def sieve(n):
    s = [True] * n
    for x in xrange(2, int(n ** 0.5) + 1):
        if s[x]:
            mark(s, x)
    return [i for i in xrange(2, n) if s[i]]
