# -*- coding: utf-8 -*-
import functions

for t in functions.gen_triangle_numbers(286):
    if functions.is_pentagonal(t) and functions.is_hexagonal(t):
        print(t)
        break
