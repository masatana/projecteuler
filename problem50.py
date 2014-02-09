#!/usr/bin/env python
# -*- coding: utf-8 -*-

from functions import *

max_primes = 0
max_primes_can = 0
max_i = 0
primes = []

for prime in gen_prime_numbers():
    primes.append(prime)
    max_primes += prime
    if is_prime(max_primes):
        print(max_primes)
    if max_primes > 1000000:
        break

def take_length(i, primes_candiate):
    for j in range(len(primes_candiate) - i):
        yield(primes_candiate[j:j+i])


for i in range(22, len(primes)):
    for can in take_length(i, primes):
        if is_prime(sum(can)):
            max_i = i if max_i < i else max_i
            max_primes_can = sum(can) if sum(can) > max_primes_can else max_primes_can
            print(max_i, max_primes_can)
