#!/usr/bin/env python3
# -*- utf-8 -*-

class Person():
    def __init__(self, name):
        self.name = name


class MDPerson(Person):
    def __init(self, name):
        self.name = 'Doctor ' + name


class JDPerson(Person):
    def __init__(self, name):
        self.name = name + ', Esquire'

person = Person('Fudd')
doctor = MDPerson('Fudd')
lawyer = JDPerson('Fudd')

class EmailPerson(Person):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email