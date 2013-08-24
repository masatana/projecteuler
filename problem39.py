# -*- coding: utf-8 -*-
import math

def check(a, b):
    c = math.sqrt(a ** 2 + b ** 2)
    if str(c).split('.')[1] == '0' and a + b + int(c) <= 1000 and b <= int(c):
        return a + b + int(c)
    else:
        return False
ans = {}

for i in range(1, 334):
    for j in range(i, 1000):
        k = check(i, j)
        if k:
            if k in ans:
                ans[k] += 1
            else:
                ans[k] = 1
mv = 0
mk = 0
for k, v in ans.items():
    print k, v
    if mv < v:
        mv = v
        mk = k
print mk


