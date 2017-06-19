#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import defaultdict

periodic_table = defaultdict(int)
periodic_table['Hydrogen'] = 1
periodic_table['Lead']

print(periodic_table)


food_count = defaultdict(int)
for food in ['spam', 'spam', 'eggs', 'spam']:
    food_count[food] += 1

for food, count in food_count.items():
    print(food, count)