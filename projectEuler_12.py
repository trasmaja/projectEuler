#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 22:13:57 2019

@author: adamlagevik
"""
import time
import math
start_time = time.time()


index = 1;
lastTri = 1;
exmaple = 5;
real = 500;
found = False;


def allFactors(num):
    global found;
    total = 0;
    maxfactor = int(math.sqrt(num));
    for x in range(1,maxfactor+1):
        if(num % x == 0):
            total += 1;
            if(x != num/x):
                total += 1;
    if(total > 500):
        print(num);
        found = True;
    
def genTri():
    allFactors(lastTri);




while(not found):
    genTri();
    index += 1;
    lastTri = lastTri + index;
    
    
print("My program took")
print(time.time() - start_time)
