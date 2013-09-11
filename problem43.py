# -*- coding: utf-8 -*-
import itertools

candidate_17 = []
candidate_13 = []
candidate_11 = []
candidate_7 = []
candidate_5 = []
candidate_3 = []
candidate_2 = []
for i in xrange(1, 1000):
    len_i = len(str(i))
    i_3 = str(i).zfill(3)
    if len(set(str(i))) == len_i and not len_i == 1:
        if i % 17 == 0:
            candidate_17.append(i_3)
        if i % 13 == 0:
            candidate_13.append(i_3)
        if i % 11 == 0:
            candidate_11.append(i_3)
        if i % 7 == 0:
            candidate_7.append(i_3)
        if i % 5 == 0:
            candidate_5.append(i_3)
        if i % 3 == 0:
            candidate_3.append(i_3)
        if i % 2 == 0:
            candidate_2.append(i_3)

def f(l1, l2):
    return [''.join(list(x[1][0]) + list(x[0])) for x in itertools.product(l1, l2) if x[0][:2] == x[1][1:3]]

tmp1 = f(candidate_17, candidate_13)
tmp2 = f(tmp1, candidate_11)
tmp3 = f(tmp2, candidate_7)
tmp4 = f(tmp3, candidate_5)
tmp5 = f(tmp4, candidate_3)
tmp6 = f(tmp5, candidate_2)
ans = 0

for x in set(tmp6):
    if len(set(x)) == 9:
        for i in range(0, 10):
            if not str(i) in x:
                ans += int(str(i) + x)

print ans
