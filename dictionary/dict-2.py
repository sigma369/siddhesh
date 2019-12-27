# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 21:10:43 2019

@author: sigma
"""
fname = input("Enter file name_\n")
fhandle = open(fname)

bag = dict()

for line in fhandle:
    
    line=line.rstrip()
    sack=line.split(" ")
    
    if sack[0] == "From":
    
        if sack[2] in bag:
            bag[sack[2]] = bag[sack[2]] + 1
        else:
            bag[sack[2]] = 1
    else:
        continue

for keys in bag:
    print (keys,bag[keys])
    
        
        
        
        
        
        
        
        
        