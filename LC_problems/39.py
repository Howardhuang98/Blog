#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   39.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/3/22 14:56  
------------      
"""
from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = [0] + heights + [0]
        ans, stack = 0, [] # (idx, height)

        for idx, height in enumerate(heights):
            print(stack)
            # 当前柱子高度比前一个柱子低
            while stack and height < stack[-1][1]:
                pre_idx, pre_height = stack.pop()
                ans = max(ans, (idx - stack[-1][0] - 1) * pre_height) # 新遍历到的，与再前一个，夹逼一下
            stack.append((idx, height))

        return ans

if __name__ == '__main__':
    s = Solution()
    s.largestRectangleArea([2,1,5,6,2,3])