#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 20:23:03 2019

@author: adamlagevik
"""

#max = 20;
max = 20;
found = False;
number = 2;

def isDiv(num):
    global number;
    for x in range(max):
        if(x == 0):
            continue;
        if(num % x != 0):
            number += 2
            return False;
        
    
    return True;

while(not found):
    if(isDiv(number)):
        print(number);
        found = True;