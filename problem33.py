# -*- coding: utf-8 -*-

def f(x, y):
    xi = [int(i) for i in list(str(x))]
    yi = [int(i) for i in list(str(y))]

ans = []

for x in range(10, 101):
    for y in range(10, 101):
        if f(x, y):
            ans.append((x, y))

print ans
