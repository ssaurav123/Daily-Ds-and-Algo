# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 01:45:37 2018

@author: shubham
"""
def LCS(A, B):
    lcs  = [[0]*(len(B)+1)for i in range(len(A)+1)]
    for i in range(1, len(A)+1):
        for j in range(1, len(B)+1):
            if A[i-1]==B[j-1]:
                lcs[i][j]=lcs[i-1][j-1]+1
            else:
                lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
    return lcs[len(A)][len(B)]


X = "AGGTAB"
Y = "GXTXAYB"

print("Length of LCS is ", LCS(X, Y))