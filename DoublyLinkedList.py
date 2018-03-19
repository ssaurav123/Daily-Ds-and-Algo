#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 20:01:28 2018

@author: shubham
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def push(self, new_data):
        New_Node = Node(new_data)
        New_Node.next = self.head
        if self.head is not None:
            self.head.prev = New_Node
        self.head = New_Node
    def InsertAfter(self, prev_node, new_data):
        New_Node = Node(new_data)
        if prev_node is None:
            print("previous node can't be none")
            return
        New_Node.next=prev_node.next
        New_Node.prev = prev_node
        prev_node.next = New_Node
        if New_Node.next is not None:
            New_Node.next.prev = New_Node
    def append(self, new_data):
        new_node = Node(new_data)
        new_node.next = None
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return
        last = self.head
        while(last.next is not None):
            last = last.next
        last.next = new_node
        new_node.prev = last
        return