#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 20:39:48 2018

@author: shubham
"""
class node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def push(self, new_data):
        New_Node = node(new_data)
        New_Node.next = self.head
        self.head = New_Node
    def InsertAfter(self, prev_node, new_node):
        if prev_node is None:
            print("node does not exist")
            return
        New_Node = node(new_node)
        New_Node.next = prev_node.next
        prev_node.next = New_Node
    def Append(self, data):
        New_Node = node(data)
        if self.head is None:
            self.head = New_Node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = New_Node
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next    
            
if __name__=='__main__':
 
    # Start with the empty list
    llist = LinkedList()
 
    # Insert 6.  So linked list becomes 6->None
    llist.Append(6)
 
    # Insert 7 at the beginning. So linked list becomes 7->6->None
    llist.push(7);
 
    # Insert 1 at the beginning. So linked list becomes 1->7->6->None
    llist.push(1);
 
    # Insert 4 at the end. So linked list becomes 1->7->6->4->None
    llist.Append(4)
 
    # Insert 8, after 7. So linked list becomes 1 -> 7-> 8-> 6-> 4-> None
    llist.InsertAfter(llist.head.next, 8)
 
    print ('Created linked list is:')
    llist.printList()