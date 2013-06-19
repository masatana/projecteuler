# -*- coding: utf-8 -*-

def check10(n):
    if list(str(n)) == list(str(n))[::-1]:
        return True
    else:
        return False

def check2(n):
    if list(str(format(n, 'b'))) == list(str(format(n, 'b')))[::-1]:
        return True
    else:
        return False

ans = 0

for n in xrange(1000000):
    if check10(n) and check2(n):
        ans += n

print ans
