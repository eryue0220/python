#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from make_db_file import storeDbase, loadDbase

db = loadDbase()

for key in db:
    print(key, '=> \n', db[key])
print(db['sue']['name'])