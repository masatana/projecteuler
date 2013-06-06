# -*- coding: utf-8 -*-

def yield_palindromic():
    for i in xrange(1, 1000000):
        reverse_i = 1000000 - i
        if str(reverse_i) == str(reverse_i)[::-1]:
            yield reverse_i

f = yield_palindromic()

def div(n):
    for i in range(100, 1000):
        for j in range(100, 1000):
            if i * j == n:
                return True
            else:
                False
for x in f:
    if div(x):
        print x
