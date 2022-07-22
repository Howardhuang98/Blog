#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   324.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/6/28 11:06  
------------      
"""
import math
from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        k = math.ceil(len(nums) / 2)
        small = [i for i in nums[:k]]
        large = [i for i in nums[k:]]
        i = 0
        while large:
            nums[i], nums[i + 1] = small.pop(), large.pop()
        if small:
            nums[-1] = small.pop()
