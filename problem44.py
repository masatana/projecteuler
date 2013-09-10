# -*- coding: utf-8 -*-
import itertools

dic = {}
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

def h(n):
    return n * (3 * n - 1) / 2

def check(n):
    i = 1
    while True:
        c = 2 * n - 3 * i ** 2 + i
        if  c == 0:
            return True
        elif c > 0:
            return False
        else:
            i += 1


for d in g():
    i = 1
    print(d)
    while (3 * i - 2) < d:
        for j in range(1, i):
            if check(dic.setdefault(i, h(i)) + dic.setdefault(j, h(j))):
                print(d)
                exit()
            print(i, j)
        i += 1
