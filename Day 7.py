# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 14:41:58 2023

@author: Sai khairnar
"""

name = "Sai"
friend = "Rakesh"
anotherFriend = 'prerna'
apple = '''She is good girl
Hi Sai,How are you
"I want to eat an apple'''
 
print("Hello, " + name)
# print(apple) 
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
# print(name[5]) # Throws an error
print("Lets use a for loop")
for character in apple:
    print(character);

for name in friend:
    print (name);