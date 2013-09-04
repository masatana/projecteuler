# -*- coding: utf-8 -*-
import functions

n = 7654321
while not(functions.is_prime(n) and functions.is_pandigital(n, 7)):
    n -= 2
print n
