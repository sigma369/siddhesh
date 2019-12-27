# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 21:09:06 2019

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
    
        if sack[1] in bag:
            bag[sack[1]] = bag[sack[1]] + 1
        else:
            bag[sack[1]] = 1
    else:
        continue
# making reverse tuple 

lst = list()
lst1 =list()

for (k,v) in (bag.items()):
    lst.append((v,k))
    lst.sort(reverse=True)
for (v,k) in lst:
    lst1.append((k,v))

print('large number of mails by',lst1[0])

















    