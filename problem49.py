# -*- coding: utf-8 -*-

import functions

primes = []
for prime in functions.gen_prime_numbers():
    if prime < 1000:
        continue
    elif prime > 10000:
        break
    else:
        primes.append(prime)
i = 0
for prime in primes:
    for prime2 in primes:
        if prime <= prime2:
            continue
        tmp = prime2 + (prime2 - prime)
        if tmp in primes:
            if set(str(prime)) == set(str(prime2)) and set(str(prime)) == set(str(tmp)):
                print(prime, prime2, tmp)
                break
