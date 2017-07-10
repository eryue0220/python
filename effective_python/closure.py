#!/usr/bin/env pyhon3
# -*- coding: utf-8 -*-

def sort_priority(numbers, group):
    found = False
    def helper(x):
        nonlocal found
        if x in group:
            found = True
            return (0, x)
        
        return (1, x)
    numbers.sort(key = helper)
    return found


number = [8, 3, 1, 2, 5, 4, 7, 6]
group = {2, 3, 5, 7}

sort_priority(number, group)
print(number)
print(type(group))