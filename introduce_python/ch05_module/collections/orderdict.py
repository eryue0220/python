#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import OrderedDict

quotes = OrderedDict([
    ('Moe', 'A  wise guy, huh?'),
    ('Larry', 'Ow!'),
    ('Curly', 'Nyuk nyuk!')
])

for stooge in quotes:
    print(stooge)
