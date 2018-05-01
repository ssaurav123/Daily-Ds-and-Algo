# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 01:25:48 2018

@author: shubham
"""
def LIS(a):
    lis = [1]*len(a)
    for i in range(len(a)):
        for j in range(i):
            if a[j]<a[i] and lis[i]<lis[j]+1:
                lis[i] = lis[j]+1
    return max(lis)
    
    
arr = [10, 22, 9, 33, 21, 50, 41, 60]
print("Length of lis is", LIS(arr))