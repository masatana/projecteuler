# -*- coding: utf-8 -*-

number = 600851475143
i = 3
factors = []
product = 1

while True:
    if number % i == 0:
        factors.append(i)
        product *= i
        number /= i
        if product >= number:
            break
    i += 2

print factors
print number
