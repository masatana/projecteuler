# -*- coding: utf-8 -*-
import itertools

def f(n):
    i = 1
    while True:
        if n < i:
            break
        yield i * (3 * i - 1) / 2
        i += 1

def g():
    i = 1
    while True:
        yield i * (3 * i - 1) / 2
        i += 1

def check(n):
    pass

dic = {}

for d in g():
    i = 1
    while (3 * i - 2) < d:
        for j in range(1, i):
            if check(f(i) + f(j)):
                print(d)
                exit()
