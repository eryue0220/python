#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

import random
import sys
import stdarray
import stdio

n = int(sys.argv[1])

count = 1
collectedCount = 0
isCollected = stdarray.create1D(n, False)

while collectedCount < n:
    value = random.randrange(0, n)
    count += 1
    if not isCollected[value]:
        collectedCount += 1
        isCollected[value] = True

stdio.writeln(count)