# -*- coding: utf-8 -*-
import itertools
import math

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
def a():
    i = 1
    while True:
        yield i * (3 * i - 1) / 2
        i += 1


def h(n):
    return n * (3 * n - 1) / 2

def check(n):
    x = (1 + math.sqrt(1 + 24 * n)) / 6.0
    return int(x) == x

def test():
    dic = []
    for d in g():
        dic.append(d)
        for e in dic:
            if check(d + e):
                print(d - e)
                if d - e in dic:
                    print(d - e)
                    exit()
if __name__ == '__main__':
    test()
