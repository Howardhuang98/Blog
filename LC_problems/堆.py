#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   堆.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/4/11 13:21  
------------      
"""
from typing import List


class heap:
    def __init__(self):
        self.nums = []

    def up(self, val):
        self.nums.append(val)
        i = len(self.nums) - 1
        pa = (i - 1) // 2
        while pa >= 0:
            if self.nums[pa] < self.nums[i]:
                self.nums[pa], self.nums[i] = self.nums[i], self.nums[pa]
                i = pa
                pa = (i - 1) // 2
            else:
                break

    def down(self,i=0):
        left = 2*i+1
        right = 2*i+2




if __name__ == '__main__':
    h = heap()
    h.add(1)
    h.add(2)
    h.add(4)
    print(h.nums)