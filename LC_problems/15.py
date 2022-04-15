#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   15.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/4/14 20:57  
------------      
"""
import itertools
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        memo = set()
        ans = []
        for i in range(len(nums)):
            if i >= 1 and nums[i] == nums[i - 1]:
                continue
            a = nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                temp = a + nums[left] + nums[right]
                if temp < 0:
                    left += 1
                elif temp == 0:
                    if (a, nums[left], nums[right]) not in memo:
                        ans.append([a, nums[left], nums[right]])
                        memo.add((a, nums[left], nums[right]))
                    right -= 1
                    left += 1
                elif temp > 0:
                    right -= 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.threeSum(nums=[-2,0,0,2,2]))
