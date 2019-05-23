#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 19:34:37 2019

@author: adamlagevik
"""

bignumber = 999;
biggestNumber = bignumber * bignumber;


def nlen(num):
    return len(str(num));

def intToArr(num):
    return list(str(num));

def isPalindrome(num):
    numArr = intToArr(num);
    for x in range(len(numArr)):
        if(numArr[x] != numArr[(len(numArr)-1-x)]):
            return False;
    return True;

def divadable(send):
    for x in range(bignumber):
        max = bignumber - x;
        if(send % max == 0 and (max > 99 and (send/max) < 999) ):
            print(max)
            return True
    
    return False

#print(divadable(997799));

for x in range(biggestNumber):
    num = biggestNumber - x;
    if(isPalindrome(num) and divadable(num)):
        print(num);
        break;