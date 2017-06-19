#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def custom_range(first = 0, last = 10, step = 1):
    number = first
    while number < last:
        yield number
        number += step

ranger = custom_range(1, 5)
for x in ranger:
    print(x)


def get_odd():
    number = []
    i = 0
    while i < 10:
        i % 2 == 1 and number.append(i)
        i += 1

    print(number)
    return number

get_odd()

