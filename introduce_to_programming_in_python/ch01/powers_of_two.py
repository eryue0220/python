#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import stdio

n = int(sys.argv[1])

power = 1
i = 0

while i <= n:
    stdio.writeln(str(i) + ' ' + str(power))
    power *= 2
    i += 1
