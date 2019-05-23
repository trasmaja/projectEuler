#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 20:41:38 2019

@author: adamlagevik
"""

example = 10;
real = 100;

sumOfSquare = 0;
squareOfSum = 0;

for x in range(real):
    x = x+1;
    sumOfSquare += x*x;
    squareOfSum += x;
    
squareOfSum = squareOfSum * squareOfSum;

diff = squareOfSum - sumOfSquare;
print(diff)