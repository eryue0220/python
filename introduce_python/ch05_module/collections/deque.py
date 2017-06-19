#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import deque

def palindrome(word):
    dq = deque(word)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    
    return True


def another_palindrome(word):
    return word == word[::-1]

