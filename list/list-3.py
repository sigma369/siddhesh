# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 20:29:14 2019

@author: sigma
"""

num = input("Enter number_\n")
sack = []
while num != 'done' :
    sack.append(num)
    num = input("Enter number_\n")
print("max of number is ",max(sack))

