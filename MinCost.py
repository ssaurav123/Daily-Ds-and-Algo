# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 00:06:48 2018

@author: shubham
"""
def MinCost(M, m, n):
    R = len(M)
    C = len(M[0])
    for i in range(1, C):
        M[0][i]+=M[0][i-1]
    for i in range(1, R):
        M[i][0]+=M[i-1][0]
    for i in range(1,m+1):
        for j in range(1,n+1):
            M[i][j] += min(M[i-1][j], M[i][j-1], M[i-1][j-1])
    return M[m][n]
    
    
cost = [[1, 2, 3],
        [4, 8, 2],
        [1, 5, 3]]
print(MinCost(cost, 2, 2))