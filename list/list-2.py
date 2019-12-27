# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 21:30:57 2019

@author: sigma
"""
fname= input('Enter file name_\n')
try:
    fhandle = open (fname)
except:
    print('file can not be open')
    raise SystemExit
sack=[]
for line in fhandle:
    line=line.rstrip()
    if "From:" in line:
        mail = line.split(" ")
        print(mail[1])
        sack.append(mail[1])
        
    else:
        continue

        
