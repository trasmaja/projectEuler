# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
max = 100000

fibonaci = []
sum = 0

def genFibo(number):
    global sum
    if(number == 1 or number == 2):
        fibonaci.append(number)
    elif(len(fibonaci) >= 2):
        two = fibonaci[len(fibonaci)-2]
        one = fibonaci[len(fibonaci)-1]
        fibonaci.append(one+two)
        if(one+two % 2 == 0):
            sum += one+two


for x in range(max):
    genFibo(x)


print(sum)
