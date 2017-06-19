#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import itertools


for item in itertools.accumulate([1, 2, 3, 4], lambda a, b: a * b):
    print(item)


def multiple(a, b):
    return a * b

for item in itertools.accumulate([1, 2, 3, 4], multiple):
    print(item)


for item in itertools.accumulate([1, 2, 3, 4]):
    print(item)


for item in itertools.chain([1, 2], ['a', 'b']):
    print(item)


for item in itertools.cycle([1, 2]):
    print(item)
