# -*- coding: utf-8 -*-
import math

mat = {1:1, 2:1}

def fib(n):
    if n in mat:
        return mat[n]
    tmp = fib(n - 1) + fib(n - 2)
    mat[n] = tmp
    return tmp

n = 1
while True:
    print n
    if math.log10(fib(n)) > 999:
        print n
        break
    n += 1

