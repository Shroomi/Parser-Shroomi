#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 16:47:56 2017

@author: mengruding
"""

class State:
    def __init__(self, heads):
        self.buffer = []
        self.stack = []
        self.trans = []
        self.heads = heads
        self.arc_gold = {}
    
    def init_configuration(self):
        self.arc_gold = {}
        for i in range(len(self.heads)):
            if int(self.heads[i]) not in self.arc_gold:
                self.arc_gold[int(self.heads[i])] = [i + 1]
            else:
                self.arc_gold[int(self.heads[i])].append(i + 1)
        
    def update(self, stack, buffer, trans):
        self.stack.append(stack)
        self.buffer.append(buffer)
        self.trans.append(trans)

class Transition:
    def __init__(self, arc_gold):
        self.arc_gold = arc_gold
        
    def can_left_arc(self, stack, buffer):
        if buffer[0] in self.arc_gold and stack[-1] in self.arc_gold[buffer[0]]:
            return True
        else:
            return False
    
    def can_right_arc(self, stack, buffer):
        s1 = set()
        if buffer[0] in self.arc_gold:
            s1 = set(self.arc_gold[buffer[0]])
        s2 = set(buffer)
        if stack[-1] in self.arc_gold and buffer[0] in self.arc_gold[stack[-1]] and len(s1.intersection(s2)) == 0:
            return True
        else:
            return False
    
    def oracle_parsing(self, stack, buffer, trans):
        if len(stack) != 0 and self.can_left_arc(stack, buffer):
            trans = 'left_arc'
            #print (str(buffer[0]) + '->' + str(stack[-1]))
            stack.pop()
        elif len(stack) != 0 and self.can_right_arc(stack, buffer):
            trans = 'right_arc'
            #print (str(stack[-1]) + '->' + str(buffer[0]))
            buffer.pop(0)
            buffer.insert(0, stack.pop())
        else:
            trans = 'shift'
            stack.append(buffer.pop(0))
        return stack, buffer, trans