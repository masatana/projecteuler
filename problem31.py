# -*- coding: utf-8 -*-
# Bad solution!
cnt = 0

for h in range(0, 200 / 200 + 1):
    tmp = 200 * h
    if tmp > 200:
        break
    for g in range(0, 200 / 100 + 1):
        tmp = 200 * h + 100 * g
        if tmp > 200:
            break
        for f in range(0, 200 / 50 + 1):
            tmp = 200 * h + 100 * g + 50 * f
            if tmp > 200:
                break
            for e in range(0, 200 / 20 + 1):
                tmp = 200 * h + 100 * g + 50 * f + 20 * e
                if tmp > 200:
                    break
                for d in range(0, 200 / 10 + 1):
                    tmp = 200 * h + 100 * g + 50 * f + 20 * e + 10 * d
                    if tmp > 200:
                        break
                    for c in range(0, 200 / 5 + 1):
                        tmp = 200 * h + 100 * g + 50 * f + 20 * e + 10 * d + 5 * c
                        if tmp > 200:
                            break
                        for b in range(0, 200 / 2 + 1):
                            tmp = 200 * h + 100 * g + 50 * f + 20 * e + 10 * d + 5 * c + 2 * b
                            if tmp > 200:
                                break
                            for a in range(0, 200 / 1 + 1):
                                tmp = a + 2 * b + 5 * c + 10 * d + 20 * e + 50 * f + 100 * g + 200 * h
                                if tmp == 200:
                                    cnt += 1
                                elif tmp > 200:
                                    break
                                
print cnt

