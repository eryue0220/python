#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def document_it(func):
    def new_func(*args, **kwargs):
        print('Running Function: ', func.__name__)
        print('Positional arguments: ', args)
        print('Keyword arguments: ', kwargs)
        result = func(*args, **kwargs)
        print('Result', result)
        return result

    return new_func

def add_int(a, b):
    return a + b

add_int(3, 5)

cooler_add_int = document_it(add_int)
cooler_add_int(3, 5)

@document_it
def add_two_num(a, b):
    return a + b

add_two_num(3, 5)
