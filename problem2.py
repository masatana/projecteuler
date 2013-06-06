# -*- coding: utf-8 -*-

def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return fib(n - 2) + fib(n - 1)

def fib_yield():
    i = 1
    j = 2
    while True:
        yield (i + j)
        i, j = j, (i + j)

f = fib_yield()
answer = 2
while True:
    num_fib = f.next()
    if num_fib >= 4000000:
        break
    answer += num_fib if num_fib % 2 == 0 else 0

print answer
