#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   668.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/5/18 11:25  
------------      
"""
import bisect
import collections
import heapq
import queue


class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def cnt(j):
            res = 0
            for i in range(1, m + 1):
                res += min(res // i, n)
            return res
        return bisect.bisect_left(range(m * n), k, key=cnt)


if __name__ == '__main__':
    s = Solution()
    print(s.findKthNumber(m=45, n=12, k=471))
    print(s.findKthNumber(m=2, n=3, k=6))
