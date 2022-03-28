#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   81.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/3/28 19:45  
------------      
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        key = nums[-1]
        if target == key:
            return True
        elif target < key:
            pre = key
            for i in range(-2, -len(nums)-1,-1):
                if nums[i] != target:
                    if nums[i] > pre:
                        return False
                    pre = nums[i]
                    continue
                else:
                    return True
        elif target > key:
            pre = key
            for i in range(0, len(nums)):
                if nums[i] != target:
                    if nums[i] < pre:
                        return False
                    pre = nums[i]
                    continue
                else:
                    return True


if __name__ == '__main__':
    s = Solution()
    s.search([2,5,6,0,0,1,2],0)