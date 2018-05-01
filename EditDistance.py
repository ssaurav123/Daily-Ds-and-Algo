# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 23:25:29 2018

@author: shubham
"""
def EditDist(X, Y):
    m = len(X)
    n = len(Y)
    edist = [[0]*(n+1) for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i ==0:
                edist[i][j] = j
            elif j==0:
                edist[i][j] = i
            elif X[i-1] == Y[j-1]:
                edist[i][j] = edist[i-1][j-1]
            else:
                edist[i][j]=1+min(edist[i-1][j], edist[i][j-1], edist[i-1][j-1])
    return edist[m][n]
    
str1 = "sunday"
str2 = "saturday"
 
print(EditDist(str1, str2))