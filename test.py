# -*- coding: utf-8 -*-
#!/usr/bin/env python

import functions

for i in functions.sieve(1000000000)[::-1]:
    if len(set(str(i))) == len(str(i)):
        print i
        break
