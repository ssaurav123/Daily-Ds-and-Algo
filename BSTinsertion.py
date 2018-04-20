# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 20:56:11 2018

@author: shubham
"""

class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.data = key
def insert(r,val):
    if r is None:
        r = Node(val)
    else:
        if val >r.data:
            if r.right is None:
                r.right = Node(val)
            else:
                r.right = insert(r.right, val)
        else:
            if r.left is None:
                r.left = Node(val)
            else:
                r.left = insert(r.left, val)       
    return r

r = Node(50)
insert(r,Node(30))
insert(r,Node(20))
insert(r,Node(40))
insert(r,Node(70))
insert(r,Node(60))
insert(r,Node(80))