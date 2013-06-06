# -*- coding: utf-8 -*-

def factorial_number(n):
    if n == 1:
        return 1
    return n * factorial_number(n - 1)

print sum([int(x) for x in list(str(factorial_number(100)))])
