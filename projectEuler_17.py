#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 23 11:03:14 2019

@author: adamlagevik
"""

example = 5;
real = 1000;


str1 = "one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen" 
str2 = "twenty twenty-one twenty-two twenty-three forty fifty sixty seventy eighty ninety one hundred two hundred one thousand"
str3 = "one two three four five six seven eight nine";
str4 = "twenty thirty forty fifty sixty seventy eighty ninety";
str5 = "hundred";


test = str1.replace(" ", "");
firstTwenty = len(test);
firstNine = len(str3.replace(" ", ""));

doubleDigits = len(str4.replace(" ",""));
hundred = len(str5);










totalSum = 0;
#totalSum += firstTwenty;
totalSum += doubleDigits * 10;
totalSum += hundred * 999;
totalSum += firstNine * 100;
totalSum += len("onethousand");


print(totalSum);