#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bottle import route, run, static_file

@route('/')
def home():
    return static_file('index.html', root = '.')


@route('/echo/<thing>')
def echo(thing):
    return 'Say hi to %s!' % thing


if __name__ == '__main__':
    run(host = 'localhost', port = 9090)
