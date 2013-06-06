# -*- coding: utf-8 -*-

cnt = 0

for i in xrange(1, 1000000):
    l = list(str(i))
    if i == sum([int(x) ** 5 for x in l]):
        cnt += i
print cnt - 1
