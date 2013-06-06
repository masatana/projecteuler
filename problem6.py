# -*- coding: utf-8 -*-

tmp = sum([x ** 2 for x in xrange(1, 101)])
tmp2 = sum([x for x in xrange(1,101)]) ** 2

print tmp2 - tmp

