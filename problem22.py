# -*- coding: utf-8 -*-

data = {}

with open('./problem22_names.txt') as f:
    data = {i: name for i, name in enumerate(sorted((((f.readline()).strip().replace('"', '')).split(','))))}

alphabet_dic = {char: i for i, char in enumerate(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))}
def names_point(name):
    point = 0
    for c in list(name):
        point += alphabet_dic[c] + 1
    return point

total = 0
for k, v in data.items():
    total +=  (k + 1) * names_point(v)
print total
