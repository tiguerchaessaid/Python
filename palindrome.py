# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 14:50:44 2022

@author: etiguercha
"""

def palindrome(x):
    
    X = x
    inverse=0
    while x!=0:
        inverse=(inverse * 10) + (x % 10)
        x = x // 10

    if X == inverse:
        print("true")
    else:
        print ("false")
        
   #X = str(x)
    #    return X == X[::-1]        
    
    
    
b=122
