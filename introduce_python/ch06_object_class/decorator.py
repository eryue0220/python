#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name

    @property
    def name(self):
        print('Inside the getter')
        return self.hidden_name
    
    @name.setter
    def name(self, input_name):
        print('Inside the setter')
        self.hidden_name = input_name


fowl = Duck('Howard')
print(fowl.name)
