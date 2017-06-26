#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import sys
import stdarray
import stdio

m = int(sys.argv[1])
n = int(sys.argv[2])

perm = stdarray.create1D(n, 0)

for i in range(n):
    perm[i] = i

for i in range(m):
    r = random.randrange(i, n)
    temp = perm[r]
    perm[r] = perm[i]
    perm[i] = temp

for i in range(m):
    stdio.write(str(perm[i]) + ' ')
stdio.writeln()
