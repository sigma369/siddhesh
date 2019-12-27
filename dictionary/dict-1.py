# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 19:26:12 2019

@author: sigma
"""

fname=input("Enter file name_\n")
fhandle = open(fname)

bag =dict()

for line in fhandle:
    line=line.strip()
    sack=line.split(" ")
    for word in sack:
        if word in bag:
            bag[word]=bag[word]+1
        else:
            bag[word]=1
            
for keys in bag:
    print(keys,bag[keys])

    


            
        
        
    
