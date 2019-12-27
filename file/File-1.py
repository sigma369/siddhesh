# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 12:12:13 2019

@author: sigma
"""
fopen = input("enter file name_\n")
fhandle = open(fopen)

for line in fhandle:
    line=line.rstrip()
    line=line.upper()
    print(line)


