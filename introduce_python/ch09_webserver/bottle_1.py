#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bottle import route, run


@route('/')
def home():
    return 'It is not fancy, but it is my home page.'

if __name__ == '__main__':
    run(host = 'localhost', port = 9090)
