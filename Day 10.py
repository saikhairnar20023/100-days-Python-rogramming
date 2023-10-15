# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 15:19:03 2023

@author: Sai khairnar
"""
applePrice = 10
budget = 200
if (budget - applePrice > 50):
    print("Alexa, add 1 kg Apples to the cart.")
elif(budget - applePrice > 50):
        print("its ok you can buy")
else:
    print("Alexa, do not add Apples to the cart.")


#
a = int(input("Enter your age: "))
print("Your age is:", a)
# Conditional operators 
# >, <, >=, <=, ==, !=
# print(a>18)
# print(a<=18)
# print(a==18)
# print(a!=18)
if(a>18):
  print("You can drive")
  print("Yes")
else:
  print("You cannot drive")
  print("No")
  print("Yay!")
  

#
num = 18
if (num < 0):
    print("Number is negative.")
elif (num <= 10):
  print("Number is between 1-10")
elif (num > 10 and num <= 20):
        print("Number is between 11-20")
else:
    print("Number is greater than 20")