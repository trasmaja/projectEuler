# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

fibonaci = []
sum = 0
max = 4000000

def isLastValueUnderMax():
    if(fiboLength() == 0):
        return True
    elif(fiboLength() > 0 and fibonaci[fiboLength()-1] > max):
        return False
    else:
        return True
    
def fiboLength():
    return len(fibonaci)

def genFibo():
    global sum
    if(fiboLength() == 0):
        fibonaci.append(1)
        
    elif(fiboLength() == 1):
        fibonaci.append(2)
        sum += 2
        
    elif(fiboLength() >= 2):
        two = fibonaci[len(fibonaci)-2]
        one = fibonaci[len(fibonaci)-1]
        fibonaci.append(one+two)
        if((one+two) % 2 == 0):
            sum += one+two
    

while(isLastValueUnderMax()):
    genFibo()


print(sum)
