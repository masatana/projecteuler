# -*- coding: utf-8 -*-

with open('./problem18_numbers.txt', 'r') as f:
    dic = {i: row.strip().split() for i, row in enumerate(f.readlines())}

for i in reversed(range(len(dic))):
    j = i - 1
    if j == -1:
        break
    for k in range(len(dic[j])):
        dic[j][k] = int(dic[j][k]) + max(int(dic[j + 1][k]), int(dic[j + 1][k + 1]))

print dic
