#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Word():
    def __init__(self, text):
        self.text = text

    def __eq__(self, word2):
        self.text.lower() == word2.text.lower()


first = Word('ha')
second = Word('HA')  

print(first == second)
