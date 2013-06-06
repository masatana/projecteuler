# -*- coding: utf-8 -*-
import math

def prime():
    primes = [2, 3]
    
    for n in range(5, 21, 2):
        isPrime = True
        for i in range(1, len(primes)):
            if primes[i] ** 2 > n:
                break
            if n % primes[i] == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(n)

    return primes
tmp = 1
for i in prime():
    tmp *= i

print tmp
print tmp * 2 * 2 * 2 * 3
