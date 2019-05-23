#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 23 10:52:44 2019

@author: adamlagevik
"""
import math;

base = 2;
example = 15;
real = 1000;

whole = math.floor(math.pow(base,real));

print("hello");

test = [int(x) for x in list(str(whole))]
print(test);


sum = 0;

for x in test:
    print(x);
    sum += x;
    
print(sum);