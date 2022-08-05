#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   622.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/8/2 13:57  
------------      
"""


class MyCircularQueue:

    def __init__(self, k: int):
        self.start = 0
        self.end = 0
        self.q = [-1 for _ in range(k)]
        self.k = k
        self.flag = False

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.flag = True
            self.q[self.end] = value
            self.end += 1
            if self.end == self.k:
                self.end = 0
            return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.flag = False
            if self.end == 0:
                self.end = self.k - 1
            else:
                self.end -= 1
            return True

    def Front(self) -> int:
        if self.isEmpty():
            return False
        else:
            return self.q[self.start]

    def Rear(self) -> int:
        if self.isEmpty():
            return False
        else:
            return self.q[self.end-1]

    def isEmpty(self) -> bool:
        if self.end == self.start and not self.flag:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if self.end == self.start and self.flag:
            return True
        else:
            return False


if __name__ == '__main__':
    obj = MyCircularQueue(3)
    obj.enQueue(1)
    obj.enQueue(2)
    obj.enQueue(3)
    obj.enQueue(4)
    print(obj.Rear())
    print(obj.isFull())
    print(obj.deQueue())
    print(obj.enQueue(4))
    print(obj.Rear())
