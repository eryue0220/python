#!/usr/bin/env python3
# -*- coding: utf-8 -*-

poem = '''
There was a yound lady named Bright,
Whose speed was far faster than light;
She started one day
In a relative way,
And returned on the previous night.
'''

fout = open('relative', 'wt')
size = len(poem)
offset = 0
chunk = 100

while True:
    if offset > chunk:
        break
    fout.write(poem[offset:offset+chunk])
    offset += chunk

fout.close()
