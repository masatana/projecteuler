# -*- coding: utf-8 -*-

mat = {}

def collatz(n, i, origin):
    if n == 1:
        mat[origin] = i
        return
    if n in mat:
        mat[origin] = i + mat[n]
        return
    if n % 2 == 0:
        collatz(n / 2, i + 1, origin)
    else:
        collatz(3 * n + 1, i + 1, origin)


for i in xrange(1, 1000000):
    collatz(i, 0, i)

for k, v in sorted(mat.items(), key = lambda x:x[1], reverse = True):
    print (k, v)
    break

