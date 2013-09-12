# -*- coding: utf-8 -*-

import itertools
import functions
import sympy

def take(n, iterable):
    return list(itertools.islice(iterable, n))

for i, j, k, l in functions.ngram(range(1000000), 4):
    if len(sympy.factorint(i)) == len(sympy.factorint(j)) == len(sympy.factorint(k)) == len(sympy.factorint(l)) == 4:
        print i, j, k, l
