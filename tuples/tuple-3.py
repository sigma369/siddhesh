# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 10:53:54 2019

@author: sigma
"""
# alphabets defination for letter frequency check
lst = ("a b c d e f g h i j k l m n o p q r s t u v w x y z")
lst=lst.split(" ")

# importing file
fname = input("enter file name_\n")
fhandle = open(fname)

# making dictionary
bag =dict()
for line in fhandle:
    line=line.rstrip()
    line=line.lower()
    sack = line.split(" ")
    
    for word in sack:
        for letter in word:
            if letter in lst:
                if letter in bag:
                    bag[letter] = bag[letter] +1
                else:
                    bag[letter] = 1
            else:
                continue
# making list for sorting and final preparation
lst_frq = list()
count =int(0)
for k,v in (bag.items()):
    lst_frq.append((k,v))
    lst_frq.sort()
    count = count+ int(v)
print (lst_frq)
print (count)


               
    



