# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 22:02:11 2018

@author: shubham
"""
import math
N = int(input())
v = list(map(int, input().split()))
s = int(input())
t = math.inf
Min = [t]*(s+1)
Min[0] = 0
for i in range(s+1):
    for j in range(N):
         if v[j]<=i and Min[i-v[j]]+1<Min[i]:
             Min[i] = Min[i-v[j]]+1
print(Min[s])