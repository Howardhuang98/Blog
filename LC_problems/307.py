#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   307.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/4/4 16:52  
------------      
"""
from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        n = len(nums)
        self.n = n
        self.seg = [0] * (2**n-1)
        self.build(nums, 0, 0, n - 1)
        print(self.seg)

    def build(self, nums: List[int], node: int, s: int, e: int):
        """
        二叉树的顺序存储
        后序遍历
        """
        if s == e:
            self.seg[node] = nums[s]
            return
        mid = (s + e) // 2
        self.build(nums, node * 2 + 1, s, mid)
        self.build(nums, node * 2 + 2, mid + 1, e)
        self.seg[node] = self.seg[node * 2 + 1] + self.seg[node * 2 + 2]

    def change(self, index: int, val: int, node: int, s: int, e: int):
        if s == e:
            self.seg[node] = val
            return
        m = s + (e - s) // 2
        if index <= m:
            self.change(index, val, node * 2 + 1, s, m)
        else:
            self.change(index, val, node * 2 + 2, m + 1, e)
        self.seg[node] = self.seg[node * 2 + 1] + self.seg[node * 2 + 2]

    def range(self, left: int, right: int, node: int, s: int, e: int) -> int:
        if left == s and right == e:
            return self.seg[node]
        m = s + (e - s) // 2
        if right <= m:
            return self.range(left, right, node * 2 + 1, s, m)
        if left > m:
            return self.range(left, right, node * 2 + 2, m + 1, e)
        return self.range(left, m, node * 2 + 1, s, m) + self.range(m + 1, right, node * 2 + 2, m + 1, e)

    def update(self, index: int, val: int) -> None:
        self.change(index, val, 0, 0, self.n - 1)

    def sumRange(self, left: int, right: int) -> int:
        return self.range(left, right, 0, 0, self.n - 1)


if __name__ == '__main__':
    s = NumArray([1, 2, 3])
