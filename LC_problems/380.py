#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   380.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/4/13 16:18  
------------      
"""
import random


class RandomizedSet:

    def __init__(self):
        self.hash = {}
        self.history = []

    def insert(self, val: int) -> bool:
        if val in self.hash:
            return False
        else:
            self.hash[val] = len(self.history)
            self.history.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self.hash:
            index = self.hash[val]
            del self.hash[val]
            if index == len(self.history)-1:
                self.history.pop()
            else:
                self.history[index] = self.history[-1]
                self.hash[self.history[-1]]=index
                self.history.pop()
            return True
        else:
            return False

    def getRandom(self) -> int:
        if not self.history:
            return None
        return random.choice(self.history)

if __name__ == '__main__':
    obj = RandomizedSet()
    obj.getRandom()
    obj.remove(0)
    obj.remove(0)
    obj.insert(0)
    obj.remove(0)
    print(obj.insert(0))
    print(obj.getRandom())
