# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 21:14:22 2019

@author: sigma
"""
def chop(lst):
    ln=len(lst)
    del lst[ln-1]
    del lst[0]
    return print('None')


lst = [1,2,3,4,5,6,7,8,9]
chop(lst)
