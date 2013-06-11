# -*- coding: utf-8 -*-

def f(x, y):
    xi = [int(i) for i in list(str(x))]
    yi = [int(i) for i in list(str(y))]
    if x == y:
        return False
    if xi[1] == 0 and yi[1] == 0:
        return False
    if xi[1] == yi[1] and yi[0] != 0 and xi[0] != 0:
        if float(xi[0]) / yi[0] == float(x) / y:
            return True
        else:
            return False
    if xi[1] == yi[0] and yi[1] != 0 and xi[0] != 0:
        if float(xi[0]) / yi[1] == float(x) / y:
            return True
        else:
            return False
    if xi[0] == yi[1] and yi[0] != 0 and xi[1] != 0:
        if float(xi[1]) / yi[0] == float(x) / y:
            return True
        else:
            return False
    if xi[0] == yi[0] and yi[1] != 0 and xi[1] != 0:
        if float(xi[1]) / yi[1] == float(x) / y:
            return True
        else:
            return False
    return False

def g(m, n):
    if n == 0:
        return m
    elif m % n == 0:
        return n
    else:
        return g(n, m % n)
ans = []
for x in range(10, 101):
    for y in range(x, 101):
        if f(x, y):
            ans.append((x, y))
tmp = 1

for i in ans:
    tmp *= float(i[0]) / i[1]
print tmp
