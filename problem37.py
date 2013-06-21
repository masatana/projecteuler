# -*- coding: utf-8 -*-
import functions

def gen_left_to_right(n):
    for i in range(len(str(n)), 0, -1):
        yield int(reduce(lambda x, y: x + y, list(str(n))[:i]))

def gen_right_to_left(n):
    for i in range(0, len(str(n))):
        yield int(reduce(lambda x, y: x + y, list(str(n))[i:]))

def check(n, prime_list):
    if n < 10:
        return False
    l_n = [int(x) for x in list(str(n))]
    """
    if l_n[0] in [1, 7, 9]:
        return False
    if l_n[-1] in [1, 7, 9]:
        return False
    """
    for i in [0, 4, 6, 8]:
        if i in l_n:
            return False
    for i in gen_left_to_right(n):
        if i not in prime_list:
            return False
    for i in gen_right_to_left(n):
        if i not in prime_list:
            return False
    return True


prime_list = []
ans = 0
cnt = 0
for prime in functions.gen_prime_numbers():
    prime_list.append(prime)
    if check(prime, prime_list):
        cnt += 1
        print prime
        ans += prime
    if cnt == 11:
        break

print ans
