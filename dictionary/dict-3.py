# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 21:44:18 2019

@author: sigma

"""
fname = input("Enter file name_\n")
fhandle = open(fname)

bag = dict()

for line in fhandle:
    
    line=line.rstrip()
    sack=line.split(" ")
    
    if sack[0] == "From:":
    
        if sack[1] in bag:
            bag[sack[1]] = bag[sack[1]] + 1
        else:
            bag[sack[1]] = 1
    else:
        continue

largest = None

for keys in bag:
    number = (bag[keys])
    if largest is None or number > largest:
        largest = number
        mail = keys
    else:
        continue

print (mail ,largest)

    
    
    
    
    
    
    
