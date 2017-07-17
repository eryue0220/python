#!/usr/bin/env python3
# -*- coding: utf-8 -*-

names = ['Cecilia', 'Lise', 'Marie']
letters = [len(n) for n in names]

longest_name = None
max_letters = 0

for i, name in enumerate(names):
    count = letters[i]
    if count > max_letters:
        max_letters = count
        longest_name = name

print(longest_name)
print(max_letters)

