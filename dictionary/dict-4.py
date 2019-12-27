# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 14:22:34 2019

@author: sigma
"""
fname = input("Enter file name_\n")
fhandle = open(fname)

bag = dict()

for line in fhandle:
    
    line=line.rstrip()
    sack=line.split(" ")
    
    if sack[0] == "From":
        
        word = sack[1].split("@")
        
        if word[1] in bag:
            bag[word[1]] = bag[word[1]] + 1
        else:
            bag[word[1]] = 1
    else:
        continue

for keys in bag:
    print (keys,bag[keys])
    
    
    
    
    
    
    