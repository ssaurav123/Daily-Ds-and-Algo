# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 16:51:37 2018

@author: shubham
"""

class Node:
    def __init__(self,data): 
        self.data = data  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.data) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.data:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.data:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

def lca(root , v1 , v2):
    while(1):
        
        if root.data >=v1 and root.data<= v2:
            return root
        elif root.data >=v2 and root.data<= v1:
            return root
        elif root.data<= v1 and root.data <= v2:
            root = root.right
        else:
            root = root.left

tree = BinarySearchTree()
t = int(input())

for _ in range(t):
    x = int(input())
    tree.create(x)
v1, v2 = map(int, input().split())
print(lca(tree.root, v1, v2))