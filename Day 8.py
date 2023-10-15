# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 14:48:34 2023

@author: Sai khairnar
"""

fruit = "Mango"
mangoLen = len(fruit)
print(len(fruit))
print(mangoLen)
print(fruit[0:4]) # including 0 but not 4
print(fruit[1:4]) # including 1 but not 4
print(fruit[:5])
print(fruit[0:-3])
print(fruit[0:-1])
print(fruit[:len(fruit)-3])
print(fruit[-1:len(fruit) - 3])
print(fruit[-3:-1])

# Quick Quiz:
nm = "Sai khairnar"
print(nm[-4:-2])
