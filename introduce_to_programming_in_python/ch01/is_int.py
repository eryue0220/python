#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

num_1 = int(sys.argv[1])
num_2 = int(sys.argv[2])

result = num_1 % num_2 == 0 or num_2 % num_1 == 0
print(result)
