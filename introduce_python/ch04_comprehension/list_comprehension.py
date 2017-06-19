#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Syntax:
# [expression for item in iterator]
# [expression for item1 in iterator1 for item2 in iterator2]
# [expression for item in iterator if condition]

number_list_1 = [number for number in range(1, 6)]
print(number_list_1)

number_list_2 = [number - 1  for number in range(1, 6)]
print(number_list_2)

odd = [number for number in range(1, 6) if number % 2 == 1]
print(odd)

even = [number for number in range(1, 6) if number % 2 == 0]
print(even)

cells = [(row, col) for row in range(1, 4) for col in range(1, 3)]
print(cells)