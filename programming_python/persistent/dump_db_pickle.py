#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pickle

dbfile = open('people-pickle', 'rb')
db = pickle.load(dbfile)

for key in db:
    print(key, '=> \n', db[key])

print(db['sue']['name'])