#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   768.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/8/13 12:42  
------------      
"""
from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        target = sorted(arr)
        ans = 1
        n = len(arr)

        def depart(i, j):
            if j - i <= 1:
                return 1
            lmax = float('-inf')
            for k in range(i, j-1):
                lmax = max(arr[k], lmax)
                rmin = min(arr[k + 1:j])
                if lmax <= rmin:
                    a = depart(i, k + 1)
                    b = depart(k + 1, j)
                    return a+b
            return 1
        return depart(0,n)

if __name__ == '__main__':
    s = Solution()
    print(s.maxChunksToSorted([2, 1, 3, 4, 4,1]))
