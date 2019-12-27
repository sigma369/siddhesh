# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 14:24:39 2019

@author: sigma
"""
fopen = input("enter file name_\n")
fhandle = open(fopen)
bag = []
count =float(0)
for line in fhandle:
    if "X-DSPAM-Confidence:" in line:
        line=line.rstrip()
        delimeter = " "
        count=count+1
        sack= line.split(delimeter)
        number = float(sack[1])
        bag.append(number)

print("Average spam confidence: ",(sum(bag))/float(count))


    
        
    

