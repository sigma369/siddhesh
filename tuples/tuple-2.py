# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 10:36:42 2019

@author: sigma
"""
fname = input("Enter file name_\n")
fhandle = open(fname)

bag = dict()

# making dictionary:
for line in fhandle:
    
    line=line.rstrip()
    sack=line.split(" ")
    
    if sack[0] == "From":
        
        cbag = sack[6].split(":")
        
        if cbag[0] in bag:
            bag[cbag[0]] = bag[cbag[0]] + 1
        else:
            bag[cbag[0]] = 1
    else:
        continue

lst = list()

for k,v in (bag.items()):
    lst.append((k,v))
    lst.sort()
    print(lst[k] , lst[v])
    
    
    
    
    
    
    
    