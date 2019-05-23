#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 20:47:37 2019

@author: adamlagevik
"""
numberOfPrimes = 0;
lastPrime = 0;
count = 2;
example = 6;
real = 10001;

def dividableOnlyWithSelf(num):
    for x in range (num):
        x += 1;
        if(num % x == 0 and x != 1 and x != num):
            return False;
    return True;


while(numberOfPrimes < real):
    if(count != 2 and count % 2 == 0):
        count += 1;
        continue;
    if(dividableOnlyWithSelf(count)):
        numberOfPrimes += 1;
        lastPrime = count;
        count += 1;
    else:
        count += 1;

print(lastPrime);
print(numberOfPrimes);
