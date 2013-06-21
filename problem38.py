# -*- coding: utf-8 -*-

def check(n):
    l = [x for x in list(str(n))]
    if '0' in l:
        return False
    elif len(set(l)) == 9:
        return True
    else:
        return False

