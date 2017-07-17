#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pickle
from initdata import db

dbfile = open('people-pickle', 'wb')
pickle.dump(db, dbfile)
dbfile.close()
