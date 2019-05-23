#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 22 11:34:26 2019

@author: adamlagevik
"""

def reverse(x):
    output = ""
    for c in x: 
        print(c)
        print(output)
        print("_------")
        output = c + output
    return output


print(reverse("adam"))
        