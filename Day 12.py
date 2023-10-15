# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 15:39:43 2023

@author: Sai khairnar
"""

x = int(input("Enter the value of x: "))
# x is the variable to match
match x:
    # if x is 0
    case 0:
        print("x is zero")
    # case with if-condition
    case _ if x < 0 :
        print("case is negative")
    case _ if x> 100:
        print(x, "is greater than 100")
    case _:
        print(x)