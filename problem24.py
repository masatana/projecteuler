# -*- coding: utf-8 -*-
import math

def f(item):
    if len(item) == 1:
        yield item
    for i in range(len(item)):
        for x in f(item[:i] + item[i+1:]):
            yield item[i] + x

c = 0
for i in f('0123456789'):
    c += 1
    if c == 1000000:
        print i
        break
