#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

import sys

def more(text, numlines = 15):
    lines = text.splitlines();

    while lines:
        chunk = lines[:numlines]
        line = lines[numlines:]
        for line in chunk:
            print(line)
        
        if lines and input('More?') not in ['y', 'Y']: break
