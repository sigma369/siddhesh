# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 19:25:37 2019

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
    line = line.rstrip()
    print(line)
    delimeter=" "
    Lst=line.split(delimeter)
    for j in range(len(Lst)):
        if Lst[j] in sack :
            continue
        else:
            sack.append(Lst[j])
sack.sort()
print(sack)


            



        
            
        
    
    

    

