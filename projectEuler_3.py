#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 15:21:23 2019

@author: adamlagevik
"""

import math 

prime = 600851475143;

squareRootOfPrime = round(math.sqrt(prime));

def dividableWithSquare(num):
    global squareRootOfPrime;
    if(prime % num == 0):
        return True
    else:
        return False

def dividableOnlyWithSelf(num):
    for x in range (num):
        x += 1;
        print
        if(num % x == 0 and x != 1 and x != num):
            return False;
    return True;


for x in range(squareRootOfPrime):
    number = squareRootOfPrime - x;
    if(dividableWithSquare(number) and dividableOnlyWithSelf(number)):
        print(number);
        break;


    
    
    