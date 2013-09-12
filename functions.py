# -*- coding: utf-8 -*-
import random
import math
import doctest

def gen_triangle_numbers(n = 1):
    while True:
        yield n * (n + 1) / 2
        n += 1

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


def mark(s, x):
    for i in range(x + x, len(s), x):
        s[i] = False

def sieve(n):
    s = [True] * n
    for x in range(2, int(n ** 0.5) + 1):
        if s[x]:
            mark(s, x)
    return [i for i in range(2, n) if s[i]]
def is_prime(n, k = 10):
    if n & 1 == 0:
        return False

    d = (n -1) >> 1
    while d & 1 == 0:
        d >>= 1
    for i in range(k):
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
    if set(str(n)) == set([str(x) for x in range(1, h + 1)]):
        return True
    else:
        return False

def is_triangle(n):
    """
    >>> is_triangle(10)
    True

    >>> is_triangle(12)
    False
    """
    x = (1 + math.sqrt(1 + 8 * n)) / 2.0
    return int(x) == x

def is_pentagonal(n):
    """
    >>> is_pentagonal(12)
    True

    >>> is_pentagonal(14)
    False
    """
    x = (1 + math.sqrt(1 + 24 * n)) / 6.0
    return int(x) == x

def is_hexagonal(n):
    """
    >>> is_hexagonal(15)
    True

    >>> is_hexagonal(18)
    False
    """
    x = (1 + math.sqrt(1 + 8 * n)) / 4.0
    return int(x) == x

def is_integer(n):
    """
    >>> is_integer(1.0)
    True
    >>> is_integer(1.2)
    False
    """
    if isinstance(n, float):
        return int(n) == n
    else:
        return False

if __name__ == '__main__':
    doctest.testmod()
