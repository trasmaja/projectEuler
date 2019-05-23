#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 22:23:14 2019

@author: adamlagevik
"""
import time
import math
start_time = time.time()

example = 10;
real = 2000000;
example = real;
sum = 0;

def dividableOnlyWithSelf(num):
    for x in range (num):
        x += 1;
        if(num % x == 0 and x != 1 and x != num):
            return False;
    return True;

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(math.sqrt(n)) + 1
    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True


for x in range(2,example+1):
    if(is_prime(x)):
        sum += x;

print(sum)

print("My program took")
print(time.time() - start_time)