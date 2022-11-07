# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def removeElement(nums, val):
    i=0
    j=len(nums)-1
    while( i<=j): 
    
        if nums[i]==val:
            j=j-1
            nums.pop(i)
            nums.append(0)
            print(j)
        else:
            i=i+1
           # print ('i=',i)
    print (nums)        
    return i
  
nums = [0,1,2,2,3,0,4,2]
test=[1,2,3,4,5,6,1]
val = 2                  
removeElement(nums, val)