#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   641.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/8/15 13:06  
------------      
"""


class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.l = [None for _ in range(k)]
        self.head = 0
        self.end = 0
        self.isEmp = True
        self.isFul = False

    def insertFront(self, value: int) -> bool:
        if self.isFul:
            return False
        else:
            if self.head == 0:
                self.head = self.k - 1
            else:
                self.head -= 1

            self.l[self.head] = value
            if self.head == self.end or abs(self.end - self.head) == self.k:
                self.isFul = True
            self.isEmp = False
            return True

    def insertLast(self, value: int) -> bool:
        if self.isFul:
            return False
        else:
            if self.end == self.k:
                self.end = 1
            else:
                self.end += 1
            self.l[self.end - 1] = value
            if self.head == self.end or abs(self.end - self.head) == self.k:
                self.isFul = True
            self.isEmp = False
            return True

    def deleteFront(self) -> bool:
        if self.isEmp:
            return False
        else:
            if self.head == self.k - 1:
                self.head = 0
            else:
                self.head += 1
            if self.head == self.end or abs(self.end - self.head) == self.k:
                self.isEmp = True
            self.isFul = False
            return True

    def deleteLast(self) -> bool:
        if self.isEmp:
            return False
        else:
            if self.end == 0:
                self.end = self.k - 1
            else:
                self.end -= 1
            if self.head == self.end or abs(self.end - self.head) == self.k:
                self.isEmp = True
            self.isFul = False
            return True

    def getFront(self) -> int:
        if self.isEmp:
            return -1
        else:
            return self.l[self.head]

    def getRear(self) -> int:
        if self.isEmp:
            return -1
        else:
            return self.l[self.end - 1]

    def isEmpty(self) -> bool:
        return self.isEmp

    def isFull(self) -> bool:
        return self.isFul


if __name__ == '__main__':
    obj = MyCircularDeque(2)
    print(obj.insertFront(7))
    print(obj.deleteLast())
    print(obj.insertLast(5))
    print(obj.insertFront(0))
    print(obj.insertLast(0))
