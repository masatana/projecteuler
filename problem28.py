# -*- coding: utf-8 -*-

def gen_spiral_numbers(k):
    return 4 * (2 * k - 1) ** 2 - 12 * (k - 1)

ans = 0
for i in range(1, 502):
    ans += gen_spiral_numbers(i)
print ans - 3
