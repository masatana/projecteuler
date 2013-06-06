# -*- coding: utf-8 -*-
import math


with open('./problem13_numbers.txt') as f:
    numbers = []
    for line in f.readlines():
        numbers.append(int(line))

big_number = 0
for number in numbers:
    big_number += number
print big_number
