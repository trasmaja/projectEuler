#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 21:54:07 2019

@author: adamlagevik
"""

import math 

a = 0;
b = 0;
c = 0;

example = 12; # 3 4 = 5 // 9 + 16 = 25
real = 1000;
example = real; #for real

def test():
    for x in range(example, 0, -1):
        cSquared = pow(x,2);
        for y in range(x, 0, -1):
            for l in range(y-1, 0, -1):
                if(y*y + l*l == cSquared and x + y + l == example):
                    print(x)
                    print(y)
                    print(l)
                    return x*y*l;
    return False;

print(test());