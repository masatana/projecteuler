# -*- coding: utf-8 -*-

def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)

d = {x: factorial(x) for x in range(0, 10)}
cnt = 0

for i in range(1, 999999):
    if i == sum([d[int(x)] for x in list(str(i))]):
        cnt += i

print cnt - 1 - 2
