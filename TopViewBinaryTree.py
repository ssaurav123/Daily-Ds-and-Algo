# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 20:32:56 2018

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
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break
tree = BinarySearchTree()
t = int(input())

for _ in range(t):
    x = int(input())
    tree.create(x)



def left1(r):
    if  r.left is not None:
        left1(r.left)
    print(r.data)
def right1(r):
    print (r.data)
    if  r.right is not None:
        right1(r.right)
    
    
def topView(root):
    if root.left is not None:
        left1(root.left)
    print (root.data)
    if root.right is not None:
        right1(root.right)

print(topView(tree.root))