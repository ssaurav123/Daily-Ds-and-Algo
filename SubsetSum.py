# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 17:59:01 2018

@author: shubham
"""
def SubsetSum(s,n,total):
    dp = [[False for i in range(total+1)] for j in range(n+1)]
    for i in range(n+1):
        dp[i][0] = True
    for i in range(1, total+1):
        dp[0][i] = False
    for i in range(1,n+1):
        for j in range(1, total+1):
            dp[i][j] = dp[i-1][j]
            if j>=s[i-1]:
                dp[i][j] = dp[i-1][j] | dp[i-1][j-s[i-1]]
    return dp[n][total]


s = [3, 34, 4, 12, 5, 2]
print(SubsetSum(s, 6, 13))
            
    
    
        