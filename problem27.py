# -*- coding: utf-8 -*-
import functions
import math
l = []
for x in functions.gen_prime_numbers():
    if x > 1000:
        break
    l.append(x)

def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True

ls = []
max_ls = 0
tmp = []

for b in reversed(l):
    for a in range(-1000, 1001):
        for x in range(0, 100):
            if is_prime(x ** 2 + a * x + b):
                ls.append(1)
            else:
                break
        if len(ls) > max_ls:
            max_ls = len(ls)
            tmp = (a, b)
        ls = []
print tmp
