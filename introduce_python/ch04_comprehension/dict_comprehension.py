#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Syntax:
# { key_expression: value_expression for expression in iterable }
# { key_expression: value_expression for expression in iterable if condition }


word = 'letter'
letter_counts = {letter: word.count(letter) for letter in set(word)}
print(letter_counts)

square = {squares: squares**2 for squares in range(10)}
print(square)

titles = ['Creature of Habit', 'Crewel Fate']
plots = ['A nun turns into a monster', 'A haunted yarn shop']

print(dict(zip(titles, plots)))
