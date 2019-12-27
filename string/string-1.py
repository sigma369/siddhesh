# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 14:40:56 2019

@author: sigma
"""
line= "X-DSPAM-Confidence:0.8475"
delimeter = ":"

sack = line.split(delimeter)

num = float(sack[1])

print (num)

