#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   2.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/3/20 10:42  
------------      
"""
import math
from typing import List


class Solution:
    def maximumCandies(self, a: List[int], k: int) -> int:
        L = 0
        R = max(a) + 1
        while L < R - 1:
            M = (L + R) // 2
            s = 0
            for i in a:
                s += i // M
            if s >= k:
                L = M
            else:
                R = M
        return L


if __name__ == '__main__':
    s = Solution()
    a = s.maximumCandies([1,1,1], k=3)
    print(a)
