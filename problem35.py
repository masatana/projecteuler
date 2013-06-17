# -*- coding: utf-8 -*-
import functions

l = []
for prime in functions.gen_prime_numbers():
    if prime > 1000000:
        break
    l.append(prime)

print 
