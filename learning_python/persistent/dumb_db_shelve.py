#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import shelve
db = shelve.open('people-shelve')
for key in db:
    print(key, '=>\b', db[key])

db.close()
