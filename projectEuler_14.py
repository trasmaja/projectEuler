#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 09:31:44 2019

@author: adamlagevik
"""
example = 13;
inputForReal = example;
steps = 0;
maxSteps = 0;
maxNumber = 0;
currentNumber = 0;

def isEven(intNumber):
    return (intNumber % 2 == 0);

def ifEven(intNumber):
    return intNumber/2;

def ifOdd(intNumber):
    return ((intNumber * 3) + 1)

def recSeq(i):
    global steps;
    global maxSteps;
    global maxNumber;
    steps += 1;
    if(i == 1):
        if(steps > maxSteps):
            maxSteps = steps;
            maxNumber = currentNumber;
    else:
        if(isEven(i)):
            recSeq(ifEven(i));
        else:
            recSeq(ifOdd(i));
        

#recSeq(inputForReal);

for x in range(1,1000001):
    steps = 0;
    currentNumber = x;
    recSeq(x)
    print(x);
    
print('---------');
print(maxSteps);
print(maxNumber);