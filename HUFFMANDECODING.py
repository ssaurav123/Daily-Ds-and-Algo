# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 00:23:29 2018

@author: shubham
"""

def decodeHuff(root , s):
    
    t = ''
    r = root
    i = 0
    while i<len(s):
        
        if s[i]=='0':
            if r.left is None:
                t+=r.data
                r = root
                
            else:
                r = r.left
                i+=1
        else:
            if r.right is None:
                t+=r.data
                r = root
                
            else:
                r = r.right
                i+=1
        if i == len(s):
            t+=r.data
    print(t)
            