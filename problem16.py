# -*- coding: utf-8 -*-

num = 0

for n in list(str(2 ** 1000)):
    print n
    num += int(n)

print num
