# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 19:48:29 2018

@author: shubham
"""
class Node:
    def __init__(self, data):
        self.val = data
        self.left =  None
        self.right = None
def Bfs(root):
    if root is None:
        return
    queue = []
    queue.append(root)
    while len(queue)>0:
        print(queue[0].val, end = " ")
        t=queue.pop(0)
        if t.left is not None:
            queue.append(t.left)
        if t.right is not None:
            queue.append(t.right)
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
 
print ("Level Order Traversal of binary tree is -")
Bfs(root)