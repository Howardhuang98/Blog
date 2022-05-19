#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   462.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/5/19 14:30  
------------      
"""
import heapq
from typing import List


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        heapq.heapify(nums)
        x = heapq.nlargest(len(nums)//2,nums)[-1]
        return sum([abs(n-x) for n in nums])

if __name__ == '__main__':
    s = Solution()
    print(s.minMoves2(
        [203125577, -349566234, 230332704, 48321315, 66379082, 386516853, 50986744, -250908656, -425653504,
         -212123143]))
